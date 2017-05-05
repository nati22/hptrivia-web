var React = require('react');
var appStyles = require('../css/app.less');
var stylinStyles = require('../css/stylin.less');

module.exports = React.createClass({
   render: function(){
       return (
           <div className={stylinStyles.parent}>
               <h1 className={stylinStyles.header}>Hello, world! I'm green!</h1>
               <div>
                   <p className={appStyles.blueP}>This text will be blue</p>
               </div>
           </div>
       )
   }
});