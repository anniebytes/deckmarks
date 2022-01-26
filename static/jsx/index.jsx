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
                        linkTitle="Browse Slideshares By Technology"/><br></br>
            <RouteLink route="browse/slideshare/lifestyle" 
                        linkTitle="Browse Slideshares By Lifestyle"/><br></br>    
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