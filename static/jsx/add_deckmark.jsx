const TextInput = (props) => {
    const [input, setInput] = React.useState("");
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

// function SelectPrivate(){
// }

// function AdditionalDeckmark(){
//     function addAnotherDeckmark(){
         
//     }

//     return (
//         <div>
//             <button type="button" onClick={addAnotherDeckmark}>+ Additional Deckmark</button>
//         </div>
//     )

// }

// function SubmitDeckmark(){
//     function addDeckmark(){
//     }

//     return(
//         <button type="submit" onSubmit={addDeckmark}>
//             Save
//         </button>
//     );
// }

// function Cancel(){
// }

const AddDeckmarkForm = () => {
    return (
        <div>
            <form action="/create_deckmark" method="POST">
            <TextInput name="link" title="Link" inputType="text"/>
            <TextInput name="description" title="Description" inputType="text"/>
            <TextInput name="thumbnail" title="Thumbnail" inputType="text"/>
            <input type="submit" value="Submit" />
            </form>
        </div>
    )
}

ReactDOM.render(
    <AddDeckmarkForm/>,
    document.querySelector('#add-deckmark-form')

);