import React from 'react';
import PropTypes from "prop-types";
import TableCell from '@material-ui/core/TableCell';
import TableHead from '@material-ui/core/TableHead';
import TableRow from '@material-ui/core/TableRow';
import TableSortLabel from '@material-ui/core/TableSortLabel';
import Checkbox from "@material-ui/core/Checkbox";
import Tooltip from '@material-ui/core/Tooltip';

class EnhancedTableHead extends React.Component {
  constructor(props) {
    super(props);
  }

  sortToggle(property) {
    return event => this.props.onSortClicked(event, property);
  }

  render() {
    const {data, order, orderBy, numSelected, rowCount} = this.props;
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
          {data.map(row => (
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
    data: PropTypes.array.isRequired,
    numSelected: PropTypes.number.isRequired,
    onSortClicked: PropTypes.func.isRequired,
    order: PropTypes.string.isRequired,
    orderBy: PropTypes.string.isRequired,
    rowCount: PropTypes.number.isRequired
  };

export default EnhancedTableHead;