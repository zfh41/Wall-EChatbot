    
import * as React from 'react';


import { Button } from './Button';
import { Socket } from './Socket';


export function Content() {
    const [addresses, setAddresses] = React.useState([]);
    const [users, setUser] = React.useState([]);
    // var messageBody = document.querySelector('#messageBody');
    // messageBody.scrollTop = messageBody.scrollHeight - messageBody.clientHeight;
    
    const [imageURL, setURL]=React.useState([])
    
    
    
    function getNewAddresses() {
        
        
        
        React.useEffect(() => 
        {
            Socket.on('addresses received', (data) => {
                
                console.log("Received addresses from server: " + data['allAddresses']);
                setAddresses(data['allAddresses']);
                setUser(data['numUsers']);
                
                console.log("numusers: " + data['numUsers']);
                console.log("URL: " + data['imageURL']);
                setURL(data['imageURL']);
                console.log("imageURL: " + imageURL);
                // <img src = {address.substring(0,9)=="wall-Ebot" ? '' : {{imageURL}} } />
                // {% if address.substring(0,9) == "wall-Ebot" %}
                //     <img src = "">
                //     {% else %}
                //     <img src = {imageURL}>
                //     {% endif %}
             
                
            })
        });
    }
    
    getNewAddresses();
    

    return (
        <div>
            <h1 style={{fontFamily:"verdana", backgroundColor: "lightblue", textAlign: "center"}}>WALL-E Chat Room! ({ users } member online)</h1>
                <div class='panel-Body scroll' id='messageBody' style={{ overflow:"auto"}}></div>
         
                <ul>
                    {
                    addresses.map((address, index) => <li style= {{fontWeight: address.substring(0,9)=="wall-Ebot" ? 'bold' : 'none'}}>
                    {address}</li>)
                    }
                </ul>
            <Button />
            
            <img class="center" src="https://cdn.dribbble.com/users/37530/screenshots/2937858/drib_blink_bot.gif"/>
            <img src={imageURL}/>
        </div>
        
    );
}
