<template>
  <div class="app-container">
    <el-row type="flex" class="row-bg">
      <el-col :span="10">
        <h3>VPN connections</h3>
      </el-col>
      <el-col>
        <el-button type="success" @click="handleCreate">Add new VPN</el-button>
      </el-col>
    </el-row>
    <!--div class="filter-container">
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
        >Search</el-button
      >
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
    </el-dialog--->
  </div>
</template>

<script>
import waves from "@/directive/waves"; // waves directive
import * as moment from "moment";

export default {
  name: "VPNs",
  directives: { waves },
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
    return {};
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
