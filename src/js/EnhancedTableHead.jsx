import React from 'react';
import TableCell from '@material-ui/core/TableCell';
import TableHead from '@material-ui/core/TableHead';
import TableRow from '@material-ui/core/TableRow';
import TableSortLabel from '@material-ui/core/TableSortLabel';

class EnhancedTableHead extends React.Component {
  constructor(props) {
    super(props);
  }

  sortToggle(property) {
    return event => this.props.onSortClicked(event, property);
  }

  selectAllClicked(event) {
    if (event.target.checked)
      this.setState(state => ({selected: state.data.map((n, index) => index)}));
    else
      this.setState({selected: []});
  }

  render() {
    const {order, orderBy, numSelected, rowCount} = this.props;
    return (
      <TableHead>
        <TableRow>
          <TableCell padding="checkbox">
            <Checkbox
              indeterminate={numSelected > 0 && numSelected < rowCount}
              checked={numSelected === rowCount}
              onChange={this.selectAllClicked}
            />
          </TableCell>
          {rows.map(row => (
            <TableCell key={row.id} numeric={row.numeric}
              padding={row.disablePadding ? "none" : "default"}
              sortDirection={orderBy === row.id ? order : false}>
              <Tooltip title="Sort" placement={row.numeric ? "bottom-end" : "bottom-start"} enterDelay={300}>
                <TableSortLabel active={orderBy === row.id} direction={order} onClick={this.sortToggle(row.id)}>
                  {row.label}
                </TableSortLabel>
              </Tooltip>
            </TableCell>
          ))}
          </TableRow>
        </TableHead>
      );
    }
  }
  
  EnhancedTableHead.propTypes = {
    numSelected: PropTypes.number.isRequired,
    onSortClicked: PropTypes.func.isRequired,
    order: PropTypes.string.isRequired,
    orderBy: PropTypes.string.isRequired,
    rowCount: PropTypes.number.isRequired
  };

export default EnhancedTableHead;