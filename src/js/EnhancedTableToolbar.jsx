import React from 'react';
import PropTypes from "prop-types";
import Toolbar from '@material-ui/core/Toolbar';
import Typography from '@material-ui/core/Typography';
import IconButton from '@material-ui/core/IconButton';
import Tooltip from '@material-ui/core/Tooltip';
import FilterListIcon from '@material-ui/icons/FilterList';
import DeleteIcon from '@material-ui/icons/Delete';

class EnhancedTableToolbar extends React.Component {
  constructor(props) {
    super(props);
  }

  render() {
    const { numSelected } = this.props;
    return (
      <Toolbar>
        {numSelected > 0 ? (
          <Typography color="inherit" variant="subtitle1">
            {numSelected} selected
              </Typography>
        ) : (
            <Typography variant="h6" id="tableTitle">
              Nutrition
              </Typography>
          )}
        {numSelected > 0 ? (
          <Tooltip title="Delete">
            <IconButton aria-label="Delete">
              <DeleteIcon />
            </IconButton>
          </Tooltip>
        ) : (
            <Tooltip title="Filter list">
              <IconButton aria-label="Filter list">
                <FilterListIcon />
              </IconButton>
            </Tooltip>
          )}
      </Toolbar>
    );
  }
};

EnhancedTableToolbar.propTypes = {
  // classes: PropTypes.object.isRequired,
  numSelected: PropTypes.number.isRequired
};

// EnhancedTableToolbar = withStyles(toolbarStyles)(EnhancedTableToolbar);
export default EnhancedTableToolbar;