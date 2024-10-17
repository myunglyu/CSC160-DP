// Checkout Button



// function getCookie(name) {
//     let cookieValue = null;
//     if (document.cookie && document.cookie !== '') {
//         const cookies = document.cookie.split(';');
//         for (let i = 0; i < cookies.length; i++) {
//             const cookie = cookies[i].trim();
//             if (cookie.substring(0, name.length + 1) === (name + '=')) {
//                 cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
//                 break;
//             }
//         }
//     }
//     return cookieValue;
// }

// const csrftoken = getCookie('csrftoken');

// document.getElementById("checkoutbtn").onclick = function() {
//     var CartDetail = "";
//     var ProductIDs = document.getElementsByClassName("productID");
//     var QtyElements = document.getElementsByClassName("quantity");
//     var userpk = document.getElementById("userpk").textContent;

//     for (var i = 0; i < ProductIDs.length; i++) {
//         var selectedQty = QtyElements[i].value;
//         CartDetail += `${ProductIDs[i].textContent}@${selectedQty}]`;
//     }

//     var strCartDetail = `${userpk}%${ProductIDs.length}%${encodeURIComponent(CartDetail)}`;

//     console.log(strCartDetail);

//     var xhr = new XMLHttpRequest();
//     xhr.open("POST", "checkout/", true);
//     xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
//     xhr.setRequestHeader("X-CSRFToken", csrftoken);
//     // xhr.onreadystatechange = function() {
//     //     if (xhr.readyState === 4 && xhr.status === 200) {
//     //         alert("Cart details saved successfully!");
//     //     }
//     // };
//     xhr.send("data=" + encodeURIComponent(strCartDetail));
// }