/**
 * IndexController.js
 *
 * @file  The Index Controller
 * @author Tomás Sánchez
 * @since  06.12.2022
 */

const API_URL = "https://www.dolarsi.com/api/api.php?type=valoresprincipales";

class Dollar {
  constructor(b = "--", s = "--") {
    this.buy = b;
    this.sell = s;
  }
}

(function IndexController() {
  getDollar();
})();

function getDollar() {
  fetch(API_URL)
    .then((data) =>
      data
        .json()
        .then((result) => {
          updateDollar(result.map((x) => x.casa));
        })
        .catch((e) => console.error(e))
    )
    .catch((e) => console.error(e));
}

/**
 * Updates Dollar Data.
 *
 * @param {{official: Dollar, mep: Dollar}} data the dollar data
 */
function updateDollar(data) {
  updateDesktop(data);
  updateMobile(data);
}
// FUNCTION APIS

window.onload = BuyBlue()
function BuyBlue() {
 var buy = document.getElementById("dolar-blue-hoy-compra")
 fetch(API_URL)
    .then(Response => Response.json())
    .then(data => {
      console.log(data.result)
      buy.innerHTML += `
      <b>$<span id="dolar-blue-hoy-compra">${data[1].casa.venta}</span></b>
      `
    })
}
//Function with Dolar Today
window.onload = BuyDollarToday()
function BuyDollarToday() {
 var buyTodayDollar = document.getElementById("dollar-today-buy-header")
 fetch(API_URL)
    .then(Response => Response.json())
    .then(data => {
      console.log(data.result)
      buyTodayDollar.innerHTML += `
      <b>$<span id="dollar-today-buy-header">${data[1].casa.compra}</span></b>
      `
    })
}
window.onload = SellDollarToday()
function SellDollarToday() {
 var sellTodayDollar = document.getElementById("dollar-today-sell-header")
 fetch(API_URL)
    .then(Response => Response.json())
    .then(data => {
      console.log(data.result)
      sellTodayDollar.innerHTML += `
      <b>$<span id="dollar-today-sell-header">${data[1].casa.venta}</span></b>
      `
    })
}
//Function with Dolar MEP
window.onload = DollarMEPsell()
function DollarMEPsell() {
 var mepSell = document.getElementById("dollar-mep-sell-header")
 fetch(API_URL)
    .then(Response => Response.json())
    .then(data => {
      console.log(data.result)
      mepSell.innerHTML += `
      <b>$<span id="dollar-mep-sell-header">${data[4].casa.venta}</span></b>
      `
    })
}
window.onload = DollarMEPbuy()
function DollarMEPbuy() {
 var mepBuy = document.getElementById("dollar-mep-buy-header")
 fetch(API_URL)
    .then(Response => Response.json())
    .then(data => {
      console.log(data.result)
      mepBuy.innerHTML += `
      <b>$<span id="dollar-mep-buy-header">${data[4].casa.compra}</span></b>
      `
    })
}
//Function with Dolar Average
window.onload = BuyProm()
function BuyProm() {
 var buyPromedio = document.getElementById("dolar-promedio-hoy-compra")
 fetch(API_URL)
    .then(Response => Response.json())
    .then(data => {
      console.log(data.result)
      buyPromedio.innerHTML += `
      <b>$<span id="dolar-promedio-hoy-compra">${data[0].casa.compra}</span></b>
      `
    })
}
window.onload = SellProm()
function SellProm() {
 var sellPromedio = document.getElementById("dolar-promedio-hoy-venta")
 fetch(API_URL)
    .then(Response => Response.json())
    .then(data => {
      console.log(data.result)
      sellPromedio.innerHTML += `
      <b>$<span id="dolar-promedio-hoy-sell">${data[0].casa.venta}</span></b>
      `
    })
}
 
//Function with Dolar Exchange
window.onload = DolarExchange()
function DolarExchange() {
 var dolarExchange = document.getElementById("dolar-bolsa")
 fetch(API_URL)
    .then(Response => Response.json())
    .then(data => {
      console.log(data.result)
      dolarExchange.innerHTML += `
      <b>$<span id="dolar-bolsa">${data[4].casa.venta}</span></b>
      `
    })
}

//Function with Dolar Turist
window.onload = DolarTurist()
function DolarTurist() {
 var dolarTuristPrice = document.getElementById("dolar-turista")
 fetch(API_URL)
    .then(Response => Response.json())
    .then(data => {
      console.log(data.result)
      dolarTuristPrice.innerHTML += `
      <b>$<span id="dolar-turista">${data[6].casa.venta}</span></b>
      `
    })
}




function updateDesktop(data) {}

// TODO:
function updateMobile(data) {}
