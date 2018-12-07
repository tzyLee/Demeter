import React from 'react';
import AppBar from '@material-ui/core/AppBar';
import Toolbar from '@material-ui/core/Toolbar';
import Typography from '@material-ui/core/Typography';
import Table from '@material-ui/core/Table';
import TableBody from '@material-ui/core/TableBody';
import TableCell from '@material-ui/core/TableCell';
import TableHead from '@material-ui/core/TableHead';
import TablePagination from '@material-ui/core/TablePagination';
import TableRow from '@material-ui/core/TableRow';
import TableSortLabel from '@material-ui/core/TableSortLabel';
import Paper from '@material-ui/core/Paper';
import Checkbox from '@material-ui/core/Checkbox';
import FilterListIcon from '@material-ui/icons/FilterList';
import EnhancedTableHead from './EnhancedTableHead.jsx';
import EnhancedTable from './EnhancedTable.jsx';

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
        new Fruit('百香果', 'Class A', '埔里 大平頂', '農夫甲', '好吃'),
        new Fruit('百香果', 'Class B', '埔里 大平頂', '農夫乙', '好吃!'),
        new Fruit('百香果', 'Class C', '埔里 大平頂', '農夫丙', '好吃!!')
      ]
    }
  }

  render() {
    return (
      <EnhancedTable data={this.state.data}/>
    );
  }
}

export default Product;