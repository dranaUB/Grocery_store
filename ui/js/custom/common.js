// Define your api here
var baseApiUrl = 'https://ubgroceryportal-bcf9fac0hzdvhud8.canadacentral-01.azurewebsites.net'; // Replace with your actual Azure App Service URL
var productListApiUrl = `${baseApiUrl}/getProducts`;
var uomListApiUrl = `${baseApiUrl}/getUOM`;
var productSaveApiUrl = `${baseApiUrl}/insertProduct`;
var productDeleteApiUrl = `${baseApiUrl}/deleteProduct`;
var orderListApiUrl = `${baseApiUrl}/getAllOrders`;
var orderSaveApiUrl = `${baseApiUrl}/insertOrder`;
// For product drop in order
var productsApiUrl = 'https://fakestoreapi.com/products';

function callApi(method, url, data) {
    $.ajax({
        method: method,
        url: url,
        data: data
    }).done(function( msg ) {
        window.location.reload();
    });
}

function calculateValue() {
    var total = 0;
    $(".product-item").each(function( index ) {
        var qty = parseFloat($(this).find('.product-qty').val());
        var price = parseFloat($(this).find('#product_price').val());
        price = price*qty;
        $(this).find('#item_total').val(price.toFixed(2));
        total += price;
    });
    $("#product_grand_total").val(total.toFixed(2));
}

function orderParser(order) {
    return {
        id : order.id,
        date : order.employee_name,
        orderNo : order.employee_name,
        customerName : order.employee_name,
        cost : parseInt(order.employee_salary)
    }
}

function productParser(product) {
    return {
        id : product.id,
        name : product.employee_name,
        unit : product.employee_name,
        price : product.employee_name
    }
}

function productDropParser(product) {
    return {
        id : product.id,
        name : product.title
    }
}

//To enable bootstrap tooltip globally
// $(function () {
//     $('[data-toggle="tooltip"]').tooltip()
// });
