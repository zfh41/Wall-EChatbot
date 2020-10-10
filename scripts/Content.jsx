    
import * as React from 'react';


import { Button } from './Button';
import { Socket } from './Socket';


export function Content() {
    const [addresses, setAddresses] = React.useState([]);
    const [users, setUser] = React.useState([]);
    
    function getNewAddresses() {
        
        React.useEffect(() => 
        {
            Socket.on('addresses received', (data) => {
                
                console.log("Received addresses from server: " + data['allAddresses']);
                setAddresses(data['allAddresses']);
                setUser(data['User']);
                
            })
        });
    }
    
    getNewAddresses();

    return (
        <div>
            <h1>WALL-E Chat Room!</h1>
                <ul>
                    {
                    addresses.map((address, index) => <li>{address}</li>)
                    }
                </ul>
            <Button />
        </div>
        
    );
}
