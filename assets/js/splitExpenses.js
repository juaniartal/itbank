/**
 * splitExpenses.js
 *
 * @file  <DESCRIPTION>
 * @author Tomás Sánchez
 * @since  05.29.2022
 */

/**
 * @type {[{name: string, amount: string}]}
 */
var aData = [];

document
  .getElementById("splitExpensesForm")
  .addEventListener("submit", function (e) {
    // Prevent Form default submit event
    e.preventDefault();
    // Obtain form Data container
    const formData = new FormData(e.target);
    // Obtain real form data {}
    const data = Object.fromEntries(formData);

    addEntryToList(data);
    updateSplit();
    e.target.reset();
  });

function updateSplit() {
  let sum = aData.map((d) => d.amount).reduce((a, b) => Number(a) + Number(b));
  let each = sum / aData.length;

  document.getElementById("totalSum").innerHTML = sum.toLocaleString();
  document.getElementById("each").innerHTML = each.toLocaleString();
}

/**
 * Adds an entry to the list of contributors.
 *
 * @param {{name: string, amount: number}} data the form data
 */
function addEntryToList(data) {
  var oList = document.getElementById("friendsList");

  aData.push(data);

  var oItem = createListItem();

  var oAvatar = createAvatar(data);
  var oBadge = createBadge(data);

  oItem.appendChild(oAvatar);
  oItem.appendChild(oBadge);

  oList.appendChild(oItem);
}

function createListItem() {
  var oItem = document.createElement("li");

  var sClasses =
    "list-group-item d-flex justify-content-between align-items-start";

  addClasses(oItem, sClasses);

  return oItem;
}

/**
 * Adds all classes to an element.
 * @param {HTMLElement} oElement an HTML element
 * @param {string} sClasses classnames seprated by space
 */
function addClasses(oElement, sClasses) {
  var aClasses = sClasses.split(" ");
  aClasses.forEach((sClass) => oElement.classList.add(sClass));
}

/**
 * Creates an Avatar.
 *
 * @param {{name: string, amount: number}} data the form data with name and amount
 * @returns a div element
 */
function createAvatar(data) {
  var oDiv = document.createElement("div");

  addClasses(oDiv, "d-flex align-items-center");

  var oImage = createImage();

  oDiv.appendChild(oImage);
  var oName = createName(data);
  oDiv.appendChild(oName);

  return oDiv;
}

/**
 * Creates an Styled Img
 *
 * @returns an img element
 */
function createImage() {
  var oImage = document.createElement("img");
  addClasses(oImage, "rounded-circle");
  oImage.style = "width: 45px; height: 45px";
  oImage.src = `https://mdbootstrap.com/img/new/avatars/${getRandomInt(
    1,
    9
  )}.jpg`;
  return oImage;
}

/**
 * Generates a div with a name.
 *
 * @param {{name: string, amount: number}} data the form data with name and amount
 * @returns {HTMLDivElement} div element
 */
function createName(data) {
  var oDiv = document.createElement("div");
  addClasses(oDiv, "ms-3");
  var oP = document.createElement("p");
  addClasses(oP, "fw-bold mb-2");
  oP.innerHTML = `${data.name}`;
  oDiv.appendChild(oP);
  return oDiv;
}

/**
 * Generates a badge with money amount.
 *
 * @param {{name: string, amount: number}} data the form data with name and amount
 * @returns {HTMLSpanElement} span badge element
 */
function createBadge(data) {
  var oSpan = document.createElement("span");

  var aBadgesClasses = [
    "badge-info",
    "badge-warning",
    "badge-danger",
    "badge-success",
    "badge-primary",
    "badge-secondary",
  ];

  addClasses(
    oSpan,
    `badge rounded-pill ${
      aBadgesClasses[getRandomInt(0, aBadgesClasses.length - 1)] || "badge-info"
    }`
  );

  oSpan.innerHTML = `$${Number(data.amount).toLocaleString()}`;

  return oSpan;
}

/**
 * Generates a random Intenger number
 *
 * @param {int} min minimal value
 * @param {int} max max value
 * @returns a Random integer between the specified parameters
 */
function getRandomInt(min, max) {
  min = Math.ceil(min);
  max = Math.floor(max);
  return Math.floor(Math.random() * (max - min + 1)) + min;
}
