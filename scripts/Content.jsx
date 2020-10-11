    
import * as React from 'react';


import { Button } from './Button';
import { Socket } from './Socket';


export function Content() {
    const [addresses, setAddresses] = React.useState([]);
    const [users, setUser] = React.useState([]);
    var clients;
    
    function getNewAddresses() {
        
        React.useEffect(() => 
        {
            Socket.on('addresses received', (data) => {
                
                console.log("Received addresses from server: " + data['allAddresses']);
                setAddresses(data['allAddresses']);
                setUser("1");
                
                
            })
        });
    }
    
    getNewAddresses();

    return (
        <div>
            <h1 style={{fontFamily:"verdana", backgroundColor: "lightblue", textAlign: "center"}}>WALL-E Chat Room! (1 member online)</h1>
                <ul>
                    {
                    addresses.map((address, index) => <li style= {{fontWeight: address.substring(0,9)=="wall-Ebot" ? 'bold' : 'none'}}>{address}</li>)
                    }
                </ul>
            <Button />
            <img class="center" src="https://cdn.dribbble.com/users/37530/screenshots/2937858/drib_blink_bot.gif"/>
        </div>
        
    );
}
