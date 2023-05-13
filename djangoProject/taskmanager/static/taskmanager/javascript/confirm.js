    function confirmTask(){
        if (confirm("Essa ação é irreversível, deseja prosseguir?")) {
            window.location.href = "{% url 'taskmanager:delete_task' task.id %}";
        }
    }

    function confirmUser(){
        var myButton = document.getElementById("delete");
    myButton.addEventListener("click", function() {
        if (confirm("Essa ação é irreversível, deseja prosseguir?")) {
            window.location.href = "{% url 'taskmanager:delete_user' utilizador.id %}";
        }
    });
    }
