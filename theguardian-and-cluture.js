const puppeteer = require("puppeteer");
const fs = require("fs");
const moment = require('moment');
const fse = require('fs-extra');

(async () => {
  let data = [];
  const browser = await puppeteer.launch({
    headless: false,
    userDataDir: "./data",
  });
  const page = await browser.newPage();
  for (let pg = 1; pg <= 1; pg++) {
    await page.goto(
      `https://www.theguardian.com/au/culture`
    );

    let listSelector = [".fc-item__kicker", ".js-headline-text"];
    for (selector of listSelector) {
      await page.waitForSelector(selector);
      let titles = await page.$$eval(
        selector,
        (links) => links.map((x) => x.innerText)
      );
      data = data.concat(titles);
    }
  }
  browser.close();
  await fse.outputFile(moment().format('YYYY-MM-DD') + '/theguardian-and-cluture.txt', data.join('\n\n'));
})();

