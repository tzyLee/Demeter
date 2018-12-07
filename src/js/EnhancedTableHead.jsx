import React from 'react';
import PropTypes from "prop-types";
import TableCell from '@material-ui/core/TableCell';
import TableHead from '@material-ui/core/TableHead';
import TableRow from '@material-ui/core/TableRow';
import TableSortLabel from '@material-ui/core/TableSortLabel';
import Checkbox from "@material-ui/core/Checkbox";
import Tooltip from '@material-ui/core/Tooltip';


const rows = [
  { id: "0", numeric: false, disablePadding: false, label: "水果"},
  { id: "1", numeric: false, disablePadding: false, label: "等級" },
  { id: "2", numeric: false, disablePadding: false, label: "產地" },
  { id: "3", numeric: false, disablePadding: false, label: "生產者" },
  { id: "4", numeric: false, disablePadding: false, label: "評價" }
];

class EnhancedTableHead extends React.Component {
  constructor(props) {
    super(props);
  }

  render() {
    const {
      onSelectAllClick,
      order,
      orderBy,
      numSelected,
      rowCount
    } = this.props;

    return (
      <TableHead>
        <TableRow>
          <TableCell padding="checkbox">
            <Checkbox
              indeterminate={numSelected > 0 && numSelected < rowCount}
              checked={numSelected === rowCount}
              onChange={onSelectAllClick}
            />
          </TableCell>
          {rows.map(row => {
            return (
              <TableCell
                key={row.id}
                numeric={row.numeric}
                padding={row.disablePadding ? "none" : "default"}
                sortDirection={orderBy === row.id ? order : false}
              >
                <Tooltip
                  title="Sort"
                  placement={row.numeric ? "bottom-end" : "bottom-start"}
                  enterDelay={300}
                >
                  <TableSortLabel
                    active={orderBy === row.id}
                    direction={order}
                    onClick={this.createSortHandler(row.id).bind(this)}
                  >
                    {row.label}
                  </TableSortLabel>
                </Tooltip>
              </TableCell>
            );
          }, this)}
        </TableRow>
      </TableHead>
    );
  }
}

EnhancedTableHead.prototype.createSortHandler = function(property) {
  return event => this.props.onRequestSort(event, property);
};

EnhancedTableHead.propTypes = {
  numSelected: PropTypes.number.isRequired,
  onRequestSort: PropTypes.func.isRequired,
  onSelectAllClick: PropTypes.func.isRequired,
  order: PropTypes.string.isRequired,
  orderBy: PropTypes.string.isRequired,
  rowCount: PropTypes.number.isRequired
};

export default EnhancedTableHead;