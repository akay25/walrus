<template>
  <div class="app-container">
    <el-row type="flex" class="row-bg">
      <el-col :span="10">
        <h3>Users</h3>
      </el-col>
      <el-col>
        <el-button type="success" @click="handleCreate">Add new User</el-button>
      </el-col>
    </el-row>
    <div class="filter-container">
      <el-input
        v-model="listQuery.username"
        placeholder="Search...User"
        style="width: 200px;"
        class="filter-item"
        @keyup.enter.native="handleFilter"
      />
      <el-select
        v-model="listQuery.region"
        placeholder="User's Region"
        clearable
        class="filter-item"
        style="width: 130px"
      >
        <el-option
          v-for="item in regions"
          :key="item.server"
          :label="item.region"
          :value="item.server"
        />
      </el-select>
      <el-button
        v-waves
        class="filter-item"
        type="primary"
        icon="el-icon-search"
        @click="handleFilter"
      >Search</el-button>
    </div>

    <el-table
      :key="tableKey"
      v-loading="listLoading"
      :data="facebook_users"
      border
      fit
      highlight-current-row
      style="width: 100%;"
    >
      <el-table-column label="Username" align="center" min-width="80px">
        <template slot-scope="{ row }">
          <span>{{ row.username }}</span>
          <el-tag :type="row.status | statusFilterColor">{{
            row.status | statusFilterLabel
          }}</el-tag>
        </template>
      </el-table-column>
      <el-table-column label="Password" align="center" min-width="50px">
        <template slot-scope="{ row }">
          <span>XXXXXX</span>
          <ion-icon
            v-clipboard:copy="row.password"
            v-clipboard:success="clipboardSuccess"
            class="copy"
            name="copy-outline"
            type="primary"
            icon="el-icon-document"
          />
        </template>
      </el-table-column>
      <el-table-column label="Region" min-width="30px" align="center">
        <template slot-scope="{ row }">
          <span>{{ row.region }}</span>
        </template>
      </el-table-column>
      <el-table-column label="Last Checked" min-width="40px">
        <template slot-scope="{ row }">
          <span>{{ row.last_checked | timestampToHuman }}</span>
        </template>
      </el-table-column>
      <el-table-column label="Total scraped" min-width="40px" align="center">
        <template slot-scope="{ row }">
          <span>{{ row.total_scraps }}</span>
        </template>
      </el-table-column>
      <el-table-column
        label="Actions"
        align="center"
        width="230"
        class-name="small-padding fixed-width"
      >
        <template slot-scope="{ row }">
          <ion-icon
            name="build"
            class="control-button"
            @click="handleUpdate(row)"
          />
          <ion-icon
            :name="row.enabled ? 'play-skip-forward-outline' : 'play-outline'"
            class="control-button danger"
            @click="toggleState(row)"
          />
          <ion-icon
            name="sync-outline"
            class="control-button danger"
            @click="handleRefresh(row)"
          />
          <ion-icon
            name="trash-outline"
            class="control-button danger"
            @click="handleDelete(row)"
          />
        </template>
      </el-table-column>
    </el-table>

    <el-dialog :title="textMap[dialogStatus]" :visible.sync="dialogFormVisible">
      <el-form
        ref="dataForm"
        :rules="validating_rules"
        :model="temp_user"
        label-position="left"
        label-width="120px"
        style="width: 400px; margin-left:50px;"
      >
        <el-form-item label="Username" prop="username">
          <el-input v-model="temp_user.username" />
        </el-form-item>
        <el-form-item label="Password" prop="password">
          <el-input v-model="temp_user.password" type="password" />
        </el-form-item>
        <el-form-item label="User's region" prop="region">
          <el-select
            v-model="temp_user.region"
            class="filter-item"
            placeholder="Select region for user"
          >
            <el-option
              v-for="item in regions"
              :key="item.server"
              :label="item.region"
              :value="item.server"
            />
          </el-select>
        </el-form-item>
        <el-form-item label="Status">
          <el-select
            v-model="temp_user.status"
            class="filter-item"
            placeholder="Please select"
          >
            <el-option
              v-for="item in [0, 1, 2]"
              :key="item"
              :label="item | statusFilterLabel"
              :value="item"
            />
          </el-select>
        </el-form-item>
        <el-form-item label="Remark">
          <el-input
            v-model="temp_user.remark"
            :autosize="{ minRows: 2, maxRows: 4 }"
            type="textarea"
            placeholder="Please input"
          />
        </el-form-item>
      </el-form>
      <div slot="footer" class="dialog-footer">
        <el-button @click="dialogFormVisible = false">
          Cancel
        </el-button>
        <el-button
          type="primary"
          @click="dialogStatus === 'create' ? createData() : updateData()"
        >
          Confirm
        </el-button>
      </div>
    </el-dialog>
  </div>
</template>

<script>
import { fetchRegions, fetchFBUsers } from "@/api/users-credentials";
import clipboard from "@/directive/clipboard/index.js"; // use clipboard by v-directive
import waves from "@/directive/waves"; // waves directive
import * as moment from "moment";

export default {
  name: "UserCredentials",
  directives: { waves, clipboard },
  filters: {
    statusFilterColor(status) {
      const statusMap = {
        1: "success",
        0: "info",
        2: "danger"
      };
      return statusMap[status];
    },
    statusFilterLabel(status) {
      const statusMap = {
        1: "Working",
        0: "Not checked",
        2: "Blocked/Dead"
      };
      return statusMap[status];
    },
    timestampToHuman(timestamp) {
      return moment.unix(timestamp).fromNow();
    }
  },
  data() {
    return {
      tableKey: 0,
      facebook_users: null,
      total: 0,
      listLoading: true,
      listQuery: {
        page: 1,
        limit: 20,
        username: undefined,
        region: undefined
      },
      regions: [],
      temp_user: {
        id: undefined,
        username: undefined,
        password: undefined,
        region: undefined,
        status: 0
      },
      dialogFormVisible: false,
      dialogStatus: "",
      textMap: {
        update: "Edit",
        create: "Add new user"
      },
      validating_rules: {
        username: [
          { required: true, message: "Username is required", trigger: "change" }
        ],
        password: [
          { required: true, message: "Password is required", trigger: "change" }
        ],
        region: [
          { required: true, message: "Region is required", trigger: "change" }
        ]
      }
    };
  },
  created() {
    this.fillPage();
  },
  methods: {
    clipboardSuccess() {
      this.$message({
        message: "Password copied",
        type: "success",
        duration: 1500
      });
    },
    fillPage() {
      this.listLoading = true;
      this.getRegions();
      this.getFBUsers();
      this.listLoading = false;
    },
    getRegions() {
      fetchRegions().then(response => {
        this.regions = response.data;
      });
    },
    getFBUsers() {
      this.listLoading = true;
      fetchFBUsers(this.listQuery).then(response => {
        this.facebook_users = response.data;
        this.listLoading = false;
      });
    },
    handleFilter() {
      this.listQuery.page = 1;
      this.getFBUsers();
    },
    resetTemp() {
      this.temp_user = {
        id: undefined,
        username: undefined,
        password: undefined,
        region: undefined,
        status: 0
      };
    },
    handleCreate() {
      this.resetTemp();
      this.dialogStatus = "create";
      this.dialogFormVisible = true;
      this.$nextTick(() => {
        this.$refs["dataForm"].clearValidate();
      });
    },
    createData() {
      // this.$refs["dataForm"].validate(valid => {
      //   if (valid) {
      //     this.temp.id = parseInt(Math.random() * 100) + 1024; // mock a id
      //     this.temp.author = "vue-element-admin";
      //     createArticle(this.temp).then(() => {
      //       this.list.unshift(this.temp);
      //       this.dialogFormVisible = false;
      //       this.$notify({
      //         title: "Success",
      //         message: "Created Successfully",
      //         type: "success",
      //         duration: 2000
      //       });
      //     });
      //   }
      // });
    },
    handleUpdate(row) {
      this.temp_user = Object.assign({}, row); // copy obj
      this.dialogStatus = "update";
      this.dialogFormVisible = true;
      this.$nextTick(() => {
        this.$refs["dataForm"].clearValidate();
      });
    },
    updateData() {
      // this.$refs["dataForm"].validate(valid => {
      //   if (valid) {
      //     const tempData = Object.assign({}, this.temp);
      //     tempData.timestamp = +new Date(tempData.timestamp); // change Thu Nov 30 2017 16:41:05 GMT+0800 (CST) to 1512031311464
      //     updateArticle(tempData).then(() => {
      //       const index = this.list.findIndex(v => v.id === this.temp.id);
      //       this.list.splice(index, 1, this.temp);
      //       this.dialogFormVisible = false;
      //       this.$notify({
      //         title: "Success",
      //         message: "Update Successfully",
      //         type: "success",
      //         duration: 2000
      //       });
      //     });
      //   }
      // });
    },
    toggleState(row) {
      this.$notify({
        title: "Success",
        message: "User state changed",
        type: "info",
        duration: 1500
      });
    },
    handleRefresh(row, index) {
      this.$notify({
        title: "Success",
        message: "User refreshed successfully",
        type: "info",
        duration: 1500
      });
    },
    handleDelete(row, index) {
      this.$notify({
        title: "Success",
        message: "Delete Successfully",
        type: "danger",
        duration: 1500
      });
    }
  }
};
</script>

<style scoped>
.copy {
  cursor: pointer;
}
.control-button {
  width: 20px;
  height: 20px;
  cursor: pointer;
  margin: 3px;
}
.control-button:hover {
  border: 1px solid #444040be;
  border-radius: 5px;
}
</style>
