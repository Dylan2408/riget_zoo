function update_cost(){
    let arrive = document.getElementById('id_zoo_booking_date_arrived').value

    arrive = new Date(arrive)
    days = Math.round(Math.abs(diff/(1000*60*60*24)))

    if (String(days) == "NaN"){
        let price = document.getElementById('zoo_output')
        price.innerHTML = "Ticket cost: Date not chosen"
    }else{

        let total = parseInt(adults.valve) * 40
                    + parseInt(children.valve) * 20
                    + parseInt(oaps.valve) * 25

        total = total

        let price = document.getElementById('zoo_output')
        price.innerHTML = "Zoo cost: £" + String(total)
    }
}

let adults = document.getElementById("id_hotel_booking_adults")
adults.addEventListener("change", update_cost)
let children = document.getElementById("id_hotel_booking_children")
children.addEventListener("change", update_cost)
let oaps = document.getElementById("id_hotel_booking_oaps")
oaps.addEventListener("change", update_cost)