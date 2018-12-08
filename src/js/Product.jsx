import React from 'react';
import AppBar from '@material-ui/core/AppBar';
import Toolbar from '@material-ui/core/Toolbar';
import Typography from '@material-ui/core/Typography';
import MUIDataTable from "mui-datatables";

class Fruit {
  constructor(name, rank, origin, farmer, remark) {
    Fruit.counter = ++Fruit.counter || 1;
    this.id = Fruit.counter;
    this.name = name;
    this.rank = rank;
    this.origin = origin;
    this.farmer = farmer;
    this.remark = remark;
  }
}

class Product extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      data: [
        ['百香果', (<img src="http://eastafricaschoolserver.org/Wikipedia/images/896/89606.png" alt='照片'></img>),'Class A', '售出', '53', '2018/12/08'],
        ['百香果', (<img src="http://sherly.mobile9.com/download/media/232/nature_j5h98iw7.jpg" alt='照片'></img>),'Class B', '售出', '42', '2018/12/08'],
        ['百香果', (<img src="http://sherly.mobile9.com/download/media/210/abstract_va9z63hk.jpg" alt='照片'></img>),'Class B', '預約出價', '41', '2018/12/08'],
        ['百香果', (<img src="data:image/jpeg;base64,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" alt='照片'></img>), 'Class C', '待售', '-', '2018/12/08']
      ],
      columns: [
        {name: "水果", option: {filter: true, sort: true}},
        {name: "照片", option: {filter: true, sort: true}},
        {name: "等級", option: {filter: true, sort: true}},
        {name: "狀態", option: {filter: true, sort: true}},
        {name: "出價", option: {filter: true, sort: true}},
        {name: "登記日期", option: {filter: true, sort: true}}
      ]
    }
  }

  render() {
    return (
      <React.Fragment>
        <AppBar position="static" color="primary">
        <Toolbar>
          <Typography variant="h6" color="inherit">
            我的產品
          </Typography>
        </Toolbar>
        </AppBar>
        <MUIDataTable title={"我的產品"} columns={this.state.columns} data={this.state.data} options={Product.option}/>
      </React.Fragment>
    );
  }
}

Product.option = {
  filterType: "dropdown",
  responsive: "scroll",
  selectableRows: true,
  textLabels: {
    body: {
      noMatch: "抱歉, 找不到結果",
      toolTip: "排序",
    },
    pagination: {
      next: "下一頁",
      previous: "上一頁",
      rowsPerPage: "每頁列數:",
    },
    toolbar: {
      search: "搜尋",
      downloadCsv: "下載成CSV",
      print: "列印",
      viewColumns: "選擇顯示行",
      filterTable: "篩選資料",
    },
    filter: {
      title: "篩選",
      reset: "重設",
    },
    viewColumns: {
      title: "顯示行",
      titleAria: "顯示/隱藏 行",
    },
    selectedRows: {
      text: "rows(s) selected",
      delete: "刪除",
      deleteAria: "刪除所選列",
    },
  }
}

export default Product;