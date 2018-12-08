import ReactDom from 'react-dom';
import React from 'react';
import Product from './js/Product.jsx';
import Price from './js/Price.jsx';

ReactDom.render(window.location.hash === "#product" ? <Product/> : <Price/>, document.getElementById('root'));
