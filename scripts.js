//configure data label, type, and value
function data_director(buttonId) {

    if (buttonId == "zip_regular_search" || buttonId == "zip_regular_search") {
        const arr = document.getElementsByTagName('input');
        var data;
        for (let i = 0; i < arr.length; i++) {
            console.log(arr[i].value);
            if (arr[i].value != "") {
                data = arr[i].value;
            }
        }
    } else {
        data = null;
    }
    console.log(data);
    var data_container = { data };
    var converter = JSON.stringify(data_container);
    data_bus(converter);
}

//interaction between JavaScript and python file
function data_bus(converter) {

    //if no data in converter, send data to user
    if (!converter) {
        //need server url? trying movie server
        const myRequest = new Request("movies.json");
        fetch(myRequest)
            .then((response) => response.json())
            .then((return_data) => {

                //for every movie in the json file
                for (const movies of return_data.movies) {

                    //create a new list item
                    const list_item = document.createElement("li");

                    list_item.appendChild(document.createElement("p")).textContent = movies.title;
                    list_item.append(` can be found at theater ${movies.theater} located at ${movies.location}.`);
                }
            })

            .catch(console.error);
    } else {

        //else send data to url for py script to listen
        $.ajax({
            //need url for python to listen on
            url: "/test",
            type: "POST",
            contentType: "application/json",
            data: JSON.stringify(converter)
        });

    }

}