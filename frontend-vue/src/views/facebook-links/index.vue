<template>
  <div class="app-container">
    <el-row type="flex" class="row-bg">
      <el-col :span="10">
        <h3>Facebook Links from database</h3>
      </el-col>
      <el-col>
        <el-button
          type="success"
          @click="reloadLinks()"
        >Reload Links</el-button>
      </el-col>
    </el-row>
    <div class="filter-container">
      <el-input
        v-model="listQuery.link"
        placeholder="Search..."
        style="width: 200px;"
        class="filter-item"
        @keyup.enter.native="handleFilter"
      />
      <el-select
        v-model="listQuery.type"
        placeholder="Link type"
        clearable
        class="filter-item"
        style="width: 130px"
      >
        <el-option
          v-for="item in linkTypes"
          :key="item"
          :label="item"
          :value="item"
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
      :data="facebook_links"
      border
      fit
      highlight-current-row
      style="width: 100%;"
    >
      <el-table-column label="Link" prop="id" align="center" min-width="180px">
        <template slot-scope="{ row }">
          <span>{{ row.link }}</span>
          <el-tag :type="row.status | statusFilterColor">{{
            row.status | statusFilterLabel
          }}</el-tag>
          <a :href="row.link" target="_blank">
            <ion-icon name="arrow-redo-outline" />
          </a>
        </template>
      </el-table-column>
      <el-table-column label="Type" min-width="50px" align="center">
        <template slot-scope="{ row }">
          <span>{{ row.type }}</span>
        </template>
      </el-table-column>
      <el-table-column label="Last Checked" min-width="60px">
        <template slot-scope="{ row }">
          <span>{{ row.last_checked | timestampToHuman }}</span>
        </template>
      </el-table-column>
      <el-table-column label="Total scraped" min-width="58px" align="center">
        <template slot-scope="{ row }">
          <span>{{ row.total_scraps }}</span>
        </template>
      </el-table-column>
      <!--el-table-column
        label="Actions"
        align="center"
        width="230"
        class-name="small-padding fixed-width"
      >
        <template slot-scope="{ row, $index }">
          <ion-icon
            name="build"
            class="control-button"
            @click="handleUpdate(row)"
          />
          <ion-icon
            :name="row.enabled ? 'close' : 'checkmark'"
            class="control-button danger"
            @click="toggleState(row)"
          />
        </template>
      </el-table-column-->
    </el-table>

    <!--pagination
      v-show="total > 0"
      :total="total"
      :page.sync="listQuery.page"
      :limit.sync="listQuery.limit"
      @pagination="getList"
    /-->
  </div>
</template>

<script>
import { fetchLinkTypes, fetchLinks, reloadLinks } from "@/api/facebook-links";
import waves from "@/directive/waves"; // waves directive
import * as moment from "moment";
// import Pagination from "@/components/Pagination"; // secondary package based on el-pagination

export default {
  name: "FacebookLinks",
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
    return {
      tableKey: 0,
      facebook_links: null,
      total: 0,
      listLoading: true,
      listQuery: {
        page: 1,
        limit: 20,
        link: undefined,
        type: undefined
      },
      linkTypes: []
    };
  },
  created() {
    this.fillPage();
  },
  methods: {
    fillPage() {
      this.listLoading = true;
      this.getLinkTypes();
      this.getList();
      this.listLoading = false;
    },
    getLinkTypes() {
      fetchLinkTypes().then(response => {
        this.linkTypes = response.data;
      });
    },
    getList() {
      this.listLoading = true;
      fetchLinks(this.listQuery).then(response => {
        this.facebook_links = response.data.items;
        this.total = response.data.total;
        this.listLoading = false;
      });
    },
    handleFilter() {
      this.listQuery.page = 1;
      this.getList();
    },
    reloadLinks() {
      reloadLinks().then(r => {
        location.reload();
      });
    }
    // toggleState(row) {
    //   this.$message({
    //     message: "操作Success",
    //     type: "success"
    //   });
    //   row.status = status;
    // }
  }
};
</script>

<style scoped>
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
