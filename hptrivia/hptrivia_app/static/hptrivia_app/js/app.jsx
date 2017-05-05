var React = require('react');
var styles = require('../css/app.css');

module.exports = React.createClass({
   render: function(){
       return (
           <div>
               <h1>Hello, world!</h1>
               <div className='blue-p'>
                   <p className={styles.blueP}>This text will be blue</p>
               </div>
           </div>
       )
   }
});