    
import * as React from 'react';


import { Button } from './Button';
import { Socket } from './Socket';


export function Content() {
    const [addresses, setAddresses] = React.useState([]);
    const [users, setUser] = React.useState([]);
    // var messageBody = document.querySelector('#messageBody');
    // messageBody.scrollTop = messageBody.scrollHeight - messageBody.clientHeight;
    
    const [imageURL, setURL]=React.useState([]);
    
    const[mURL, setmURL]=React.useState([])
    const[dbUser, setdbUser]=React.useState([])
    
    const[isURL, setisURL]=React.useState([])
    
    function getNewAddresses() {
        
        
        
        React.useEffect(() => 
        {
            Socket.on('addresses received', (data) => {
                

                setAddresses(data['allAddresses']);
                setUser(data['numUsers']);
                setdbUser(data['dbUser']);
                
                setURL(data['imageURL']);
                
                setisURL(data['isUrl']);
                
                setmURL(data['address']);
              
                // <img src = {address.substring(0,9)=="wall-Ebot" ? '' : {{imageURL}} } />
                // {% if address.substring(0,9) == "wall-Ebot" %}
                //     <img src = "">
                //     {% else %}
                //     <img src = {imageURL}>
                //     {% endif %}
             
                
            })
        });
    }
    
    function PutMessage(props)
    {
        if (isURL == 0){
            return ( <div> <p>{dbUser}</p>
                      <a href={mURL}>{props.address}</a> 
                      </div> )
        }
        else{
            return(<p style = {{display: "inline"}} >{props.address}</p>)
        }
        
        
        
    }

    
    getNewAddresses();

    return (
        <div>
            <h1 style={{fontFamily:"verdana", backgroundColor: "lightblue", textAlign: "center"}}>WALL-E Chat Room! ({ users } member online)</h1>
                <div class='panel-Body scroll' id='messageBody' style={{ overflow:"auto"}}></div>
                <ul>
                    {
                    addresses.map((address, index) => <li style= {{fontWeight: address.substring(0,9)=="wall-Ebot" ? 'bold' : 'none'}}>
                    <img src = { address.substring(0,9)=="wall-Ebot" ? "https://cdn.dribbble.com/users/37530/screenshots/2937858/drib_blink_bot.gif" : imageURL } width="30" height="30" />
                    <PutMessage address={address}/>
                    </li>)
                    }
                </ul>
            <Button />
            
            <img class="center" src="https://cdn.dribbble.com/users/37530/screenshots/2937858/drib_blink_bot.gif"/>
        </div>
        
    );
}
