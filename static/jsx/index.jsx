function RouteLink(props){
    return ( 
            <a href={props.route}>{props.linkTitle}</a>
    )
}

function UserOnlyLinks(){
    return (
        <div>
            <RouteLink route="add_group" linkTitle="Add Group"/><br></br>
            <RouteLink route="add_deckmark" linkTitle="Add Deckmark"/>
        </div>
    )
}

function LoginLinks(){
    return (
        <div>
            <RouteLink route="login" linkTitle="Login"/><br></br>
            <RouteLink route="register" linkTitle="Register"/>
        </div>
    )
}

function DeckmarksLinks(){
    return(
        <div>
            <RouteLink route="/deckmarks" linkTitle="Browse All Deckmarks"/><br></br>
            <RouteLink route="/groups" linkTitle="Browse All Groups" /><br></br>
        </div>
    )
}

function SlideshareLinks(){
    return(
        <div>
            <RouteLink route="browse/slideshare/technology" 
                        linkTitle="Browse Slideshares On Technology"/><br></br>
            <RouteLink route="browse/slideshare/lifestyle" 
                        linkTitle="Browse Slideshares On Lifestyle"/><br></br>    
            <RouteLink route="browse/slideshare/art-photos" 
                        linkTitle="Browse Slideshares On Art"/><br></br>    
            <RouteLink route="browse/slideshare/design" 
                        linkTitle="Browse Slideshares On Design"/><br></br>    
            <RouteLink route="browse/slideshare/business" 
                        linkTitle="Browse Slideshares On Business"/><br></br>    
            <RouteLink route="browse/slideshare/career" 
                        linkTitle="Browse Slideshares On Career"/><br></br>    
            <RouteLink route="browse/slideshare/economy-finance" 
                        linkTitle="Browse Slideshares On Finance"/><br></br>
            <RouteLink route="browse/slideshare/food" 
                        linkTitle="Browse Slideshares On Food"/><br></br>    
            <RouteLink route="browse/slideshare/data-analytics" 
                        linkTitle="Browse Slideshares On Data"/><br></br> 
            <RouteLink route="browse/slideshare/entertainment-humor" 
                        linkTitle="Browse Slideshares On Entertainment"/><br></br> 
            <RouteLink route="browse/slideshare/engineering" 
                        linkTitle="Browse Slideshares On Engineering"/><br></br> 
            <RouteLink route="browse/slideshare/devices-hardware" 
                        linkTitle="Browse Slideshares On Hardware"/><br></br> 
            <RouteLink route="browse/slideshare/education" 
                        linkTitle="Browse Slideshares On Education"/><br></br> 
            <RouteLink route="browse/slideshare/environment" 
                        linkTitle="Browse Slideshares On Environment"/><br></br> 
        </div>
    )
}

function DisplayIndexPage(){
    return (
        <div>
            <LoginLinks />
            <UserOnlyLinks />
            <DeckmarksLinks />
            <SlideshareLinks />
        </div>
    )
}

ReactDOM.render(
    <DisplayIndexPage />, document.querySelector('#root')
);