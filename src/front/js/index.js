/* eslint-disable */

import "../assets/img/rigo-baby.jpg";
import "../assets/img/4geeks.ico";
//import 'breathecode-dom'; //DOM override to make JS easier to use
import "../style/index.scss";

window.onload = async function() {
  const response = await fetch(
    "https://3000-dcd4c2c4-3ab1-4581-9793-454279c4b775.ws-us02.gitpod.io/api/card"
  );
  let response_body = await response.json();
  console.log(response_body);
  let suit_symbol = document.querySelector(".top div");
  console.log(suit_symbol);

  suit_symbol.innerHTML = "HEART";
};
