const Thumbnail = (props) => {

    return (
        <div>
            <img src={props.image}></img>
        </div>
    )
}


const Link = (props) => {

    return (
        <div>
            <a href={props.link}>{props.title}</a>
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


const TextInput = (props) => {
    const [input, setInput] = React.useState(props.initValue);
    return (
        <div>
            <label>
                {props.title}:
                <input type="{props.inputType}"
                    name={props.name}
                    value={input}
                    onChange={e => setInput(e.target.value)}
                />
            </label>
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


const UserDeckmarks = (props) => {
    console.log(props.user_id)
    const [deckmarks, setDeckmarks] = React.useState([]);
    React.useEffect(() => {
      fetch(`/api/user/${props.user_id}/deckmarks`)
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

const user_div = document.querySelector('.user')
const user_id = user_div.id.split('-')[1]

ReactDOM.render(
    <UserDeckmarks user_id={user_id} />,
    document.querySelector('.user')
)