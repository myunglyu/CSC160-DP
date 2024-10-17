document.getElementById("ordersubmitbtn").onclick = function(event) {
    // event.preventDefault();  // Prevent the default form submission

    var Orderdetail = "";
    var ProductIDs = document.getElementsByClassName("ordersummary_productID");
    var QtyElements = document.getElementsByClassName("ordersummary_quantity");
    var userpk = document.getElementById("userpk").textContent;

    for (var i = 0; i < ProductIDs.length; i++) {
        var selectedQty = QtyElements[i].textContent;
        Orderdetail += `${ProductIDs[i].textContent}@${selectedQty}]`;
    }

    var strOrderDetail = `${userpk}&${ProductIDs.length}&${encodeURIComponent(Orderdetail)}`;
    
    document.getElementById("ordersubmitdata").value = strOrderDetail;

    console.log(strOrderDetail);

    document.getElementById("checkoutForm").submit();
}
