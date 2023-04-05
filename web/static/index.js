$("#alrt").show().delay(1000).fadeOut();
AOS.init();
function deleteNote(noteId) {
    fetch("/delete-note", {
        method:"POST", 
        body:JSON.stringify({noteId: noteId}),
    }).then((_res) => {
        window.location.href="/notes";
    });
}
