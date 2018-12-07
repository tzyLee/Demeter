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
import IconButton from '@material-ui/core/IconButton';
import Tooltip from '@material-ui/core/Tooltip';
import DeleteIcon from '@material-ui/icons/Delete';
import FilterListIcon from '@material-ui/icons/FilterList';
import EnhancedTableHead from './EnhancedTableHead.jsx';

class Fruit {
  constructor(name, rank, origin, farmer, remark) {
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
      orderBy: 'fruitName',
      order: 'asc',
      selected: [],
      data: [
        new Fruit('百香果', 'Class A', '埔里 大平頂', '農夫甲', '好吃'),
        new Fruit('百香果', 'Class B', '埔里 大平頂', '農夫乙', '好吃!'),
        new Fruit('百香果', 'Class C', '埔里 大平頂', '農夫丙', '好吃!!')
      ],
      header: [
        { id: 0, numeric: false, disablePadding: false, label: "水果"},
        { id: 1, numeric: true, disablePadding: false, label: "等級" },
        { id: 2, numeric: true, disablePadding: false, label: "產地" },
        { id: 3, numeric: true, disablePadding: false, label: "生產者" },
        { id: 4, numeric: true, disablePadding: false, label: "評價" }
      ]
    };
  }

  selectAllClicked(event) {
    if (event.target.checked)
      this.setState(state => ({selected: state.data.map((n, index) => index)}));
    else
      this.setState({selected: []});
  }

  rowClicked(event, rowID) {
    const { selected } = this.state;
    const selectedIndex = selected.indexOf(rowID);
    let newSelected = [];
  
    if (selectedIndex === -1)
      newSelected = [...selected, rowID];
    else if (selectedIndex === 0)
      newSelected = selected.slice(1);
    else if (selectedIndex === selected.length - 1)
      newSelected = selected.slice(0, -1);
    else if (selectedIndex > 0)
      newSelected = newSelected.concat(selected.slice(0, selectedIndex), selected.slice(selectedIndex + 1));
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
      <Paper>
        <Typography variant="h6">Product List</Typography>
        <Table>
          <EnhancedTableHead data={this.state.header} order={this.state.order} orderBy={this.state.orderBy} onSortClicked={this.selectAllClicked.bind(this)} numSelected={this.state.selected.length} rowCount={this.state.data.length}/>
          <TableBody>
            {this.state.data.map((fruit, index) => (
              <TableRow key={index} hover onClick={event => this.rowClicked(event, index)}>
                <TableCell padding="checkbox">
                  <Checkbox checked={true}/>
                </TableCell>
                <TableCell>{fruit.name}</TableCell>
                <TableCell>{fruit.rank}</TableCell>
                <TableCell>{fruit.origin}</TableCell>
                <TableCell>{fruit.farmer}</TableCell>
                <TableCell>{fruit.remark}</TableCell>
              </TableRow>
            ))
            }
            {/* {stableSort(data, getSorting(order, orderBy))
              .slice(page * rowsPerPage, page * rowsPerPage + rowsPerPage)
              .map(n => {
                const isSelected = this.isSelected(n.id);
                return (
                  <TableRow
                    hover
                    onClick={event => this.handleClick(event, n.id)}
                    role="checkbox"
                    aria-checked={isSelected}
                    tabIndex={-1}
                    key={n.id}
                    selected={isSelected}
                  >
                    <TableCell padding="checkbox">
                      <Checkbox checked={isSelected} />
                    </TableCell>
                    <TableCell numeric>{n.protein}</TableCell>
                  </TableRow>
                );
              })} */}
          </TableBody>
        </Table>
      </Paper>
      </React.Fragment>
    );
  }
}

export default Product;