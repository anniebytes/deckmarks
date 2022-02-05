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

const Tag = (props) => {
    return (
        <button>{props.tag_name}</button>
    )
}


const Tags = (props) => {
    const [tags, setTags] = React.useState([]);
    const apiEndpoint = `/api/deckmark/${props.deckmark_id}/tags`
    React.useEffect(() => {
      fetch(apiEndpoint)
        .then(response => response.json())
        .then(result => {
            if (Object.keys(result).length > 0 ) {
                setTags(result);
            }
        });
    }, []);

    let tagsArray = []
    if (Object.keys(tags).length > 0) {
        tagsArray = Object.entries(tags)
    }
    
    const tagItems = tagsArray.map((tag) => {
        return <Tag tag_id={tag[0]} tag_name={tag[1]}/>
    });

    return (
        <div>
            {tagItems}
        </div>
    )
}

const AddTags = (props) => {
    console.log("add " + props.deckmark_id)

    return (
        <form action="/api/add_tag_to_deckmark" method="POST">
            <TextInput name="tag_name" title="Add Tag" inputType="text"/>
            <input type="hidden" name="deckmark_id" value={props.deckmark_id}/>
            <input type="submit" value="Add" />
        </form>
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
    console.log(props.deckmark_id)

    const [mode, setMode] = React.useState(mode);

    function editButtonClicked(e) {
        e.target.setAttribute("hidden", true);
        setMode("edit")
    }

    function cancelButtonClicked(e) {
        e.target.setAttribute("hidden", true);
        setMode("view")
    }

  const deckmarkComponents = [<Thumbnail image={props.image} key="thumbnail"/>, 
        <Link link={props.link} title={props.link} key="link"/>, 
        <Description description={props.description} key="description"/>,
        <Tags deckmark_id={props.deckmark_id} key="tags"/>,
        <UserInfo id={props.user_id} key="userinfo"/>, 
        <button type="button" onClick={editButtonClicked} key="edit">Edit</button>
    ]

    if (mode == "edit") {
        return (
            <div>
                <form action="/create_deckmark" method="POST">
                <Thumbnail image={props.image} key="thumbnail"/>
                <TextInput name="link" title="Link" inputType="text" initValue={props.link}/>
                <TextInput name="description" title="Description" inputType="text" initValue={props.description}/>
                <UserInfo id={props.user_id} key="userinfo"/>
                <input type="submit" value="Save" />
                <button type="button" onClick={cancelButtonClicked} key="cancel">Cancel</button>
                </form>
                <Tags deckmark_id={props.deckmark_id} key="tags"/>
                <AddTags deckmark_id={props.deckmark_id}/>
            </div>
        )
    }

    return (
        <div>
            {deckmarkComponents} 
        </div>
    )

}


const UserDeckmarks = (props) => {
    console.log(props.user_id)
    const [deckmarks, setDeckmarks] = React.useState([]);
    const apiEndpoint = `/api/user/${props.user_id}/deckmarks`
    React.useEffect(() => {
      fetch(apiEndpoint)
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
                    deckmark_id={deckmark.id}
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