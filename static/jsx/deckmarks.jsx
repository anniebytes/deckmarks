const Thumbnail = (props) => {

    return (
        <div>
            <img src="{props.image}"></img>
        </div>
    )
}


const Link = (props) => {

    return (
        <div>
            <a href="{props.link}">{props.title}</a>
        </div>
    )
}


const Description = (props) => {

    return (
        <div>
            <p>
                {props.description}
            </p>
        </div>
    )
}


const UserInfo = (props) => {

    return (
        <div>
            {props.id}
        </div>
    )
}


const Deckmark = (props) => {

    return (
        <div>
            <Thumbnail image={props.image}/>
            <Link link={props.link} title={props.link}/>
            <Description description={props.description}/>
            <UserInfo id={props.user_id}/>
        </div>
    )
}


const AllDeckmarks = () => {
    const [deckmarks, setDeckmarks] = React.useState([]);

    React.useEffect(() => {
      fetch('/api/deckmarks/all')
        .then(response => response.json())
        .then(result => {
          setDeckmarks(result);
        });
    }, []);

    if (deckmarks.length === 0) {
        return <p>Loading...</p>;
    }

    const deckmarkItems = deckmarks.map((deckmark) => {
        return (
            <div key={deckmark.id}>
                <Deckmark 
                    image={deckmark.thumbnail}
                    link={deckmark.link}
                    description={deckmark.description}
                    user_id={deckmark.user_id}
                />
            </div>);

    });

    return (
        <div>
            {deckmarkItems}
        </div>
    )

}


ReactDOM.render(
    <AllDeckmarks />,
    document.querySelector('#view-all-deckmarks')
)