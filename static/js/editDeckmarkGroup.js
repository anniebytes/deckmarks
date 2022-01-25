/* JS for group_details_edit.html */

const groupNameElem = document.querySelector("#group-name");
const groupNameInputElemParent = document.querySelector("#group-name-input");
const btnGroupNameEditSave = document.querySelector("#btn-group-name-edit-save");
const btnGroupNameCancel = document.querySelector("#btn-group-name-cancel")

function showInputField(textElem, inputElemParent, inputType, inputId){
    textElem.hidden = true;
    const textElemValue = textElem.innerText;

    const inputHTML = `<input id="${inputId}" type="${inputType}">`
    inputElemParent.innerHTML = inputHTML;

    const inputElem = document.querySelector(`#${inputId}`)
    inputElem.defaultValue = textElemValue;
    inputElemParent.hidden = false;
}

function showOriginalElem(originalElem, inputElemParent){
    originalElem.hidden = false;
    inputElemParent.hidden = true;
}

function changeToSaveButton(buttonElem){
    buttonElem.value = 'save'; 
    buttonElem.innerText = 'Save';
}

function changeToEditButton(buttonElem){
    buttonElem.value = 'edit'; 
    buttonElem.innerText = 'Edit';
}

function hideCancelButton(buttonElem){
    buttonElem.hidden = true;
}

function showCancelButton(buttonElem){
    buttonElem.hidden = false;
}

function sendToServer(data, route){
    fetch(route, {
        method: 'POST', 
        body: JSON.stringify({data: data}), 
        headers: {'Content-Type': 'application/json'},
    })
    .then ( response => response.json())
    .then ( responseData => {
        console.log(responseData.status);
    })
}

function updateGroupNameDB(groupName, newName){
    const jsonData = {
        'group_name': groupName.innerText,
        'new_group_name': newName,  
    };
    sendToServer(jsonData, '/api/update_group_name');
}

btnGroupNameEditSave.addEventListener('click', (evt) => {
    targetButton = evt.target;
    if (targetButton.value == 'edit') {
        showInputField(groupNameElem, groupNameInputElemParent, "text", "group-name-input-field");
        changeToSaveButton(btnGroupNameEditSave);
        showCancelButton(btnGroupNameCancel);
    }

    else if (targetButton.value == 'save') {
        changeToEditButton(btnGroupNameEditSave);
        showOriginalElem(groupNameElem, groupNameInputElemParent);
        hideCancelButton(btnGroupNameCancel);

        const inputValue = document.querySelector("#group-name-input-field").value;
        updateGroupNameDB(groupNameElem, inputValue);
        groupNameElem.innerText = inputValue;
        console.log("New group name sent to server.");
    }
})
 
btnGroupNameCancel.addEventListener('click', (evt) => {
    showOriginalElem(groupNameElem, groupNameInputElemParent);
    changeToEditButton(btnGroupNameEditSave);
    hideCancelButton(evt.target);
})