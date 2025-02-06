const editButtons = document.getElementsByClassName("btn-edit");
const commentText = document.getElementById("id_comment");
const commentForm = document.getElementById("commentForm");
const submitButton = document.getElementById("submitButton");

/**
* Initializes edit functionality for the provided edit buttons.
* 
* For each button in the `editButtons` collection:
* - Retrieves the associated comment's ID upon click.
* - Fetches the content of the corresponding comment.
* - Populates the `commentText` input/textarea with the comment's content for editing.
* - Updates the submit button's text to "Update".
* - Sets the form's action attribute to the `edit_comment/{commentId}` endpoint.
*/
for (let button of editButtons) {
  button.addEventListener("click", (e) => {
    let commentId = e.target.getAttribute("data-comment-id");
    let commentContent = e.target.getAttribute("data-comment-text");
    commentText.value = commentContent;
    submitButton.innerText = "Update";
    commentForm.setAttribute("action", `edit_comment/${commentId}`);
    document.getElementById('comment-form-card').scrollIntoView({ behavior: 'smooth' });
  });
}

