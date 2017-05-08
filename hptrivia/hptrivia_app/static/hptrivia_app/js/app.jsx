var React = require('react');
var $ = require('jquery');
var appStyles = require('../css/app.less');
var stylinStyles = require('../css/stylin.less');
var FullPageStyles = require('../css/vendor/jquery.fullpage.css');
var FullPage = require('fullpage.js');

module.exports = React.createClass({
   render: function(){
       return (
           <div id="fullpage" style={{backgroundColor: 'black'}}>
                <h1 className="section" style={{color: 'yellow', backgroundColor: 'green'}}>1</h1>
                <h1 className="section" style={{color: 'yellow', backgroundColor: 'blue'}}>2</h1>
                <h1 className="section" style={{color: 'yellow'}}>3</h1>
                <h1 className="section" style={{color: 'yellow'}}>4</h1>
            </div>
       )
   },
    componentDidMount: function () {
        $(document).ready(function() {
            $('#fullpage').fullpage({
                keyboardScrolling: false,
                dragAndMove: false
            });
            $.fn.fullpage.setMouseWheelScrolling(false);
            $.fn.fullpage.setAllowScrolling(false);
        });
    }
});

