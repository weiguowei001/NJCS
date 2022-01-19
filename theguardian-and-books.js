const puppeteer = require("puppeteer");
const fs = require("fs");
const moment = require('moment');
const fse = require('fs-extra');

(async () => {
  let data = [];
  const browser = await puppeteer.launch({
    headless: false,
    userDataDir: "./data"
  });
  const page = await browser.newPage();
  await page.setDefaultNavigationTimeout(0);
  for (let pg = 1; pg <= 1; pg++) {
    await page.goto(
      `https://www.theguardian.com/books`
    );

    let listSelector = [".fc-item__link > span:nth-child(-n+2)"];
    for (selector of listSelector) {
      await page.waitForSelector(selector);
      data = await page.$$eval(
        selector,
        (links) => links.map((x) => x.innerText)
      );
    }
  }
  browser.close();
  await fse.outputFile(moment().format('YYYY-MM') + '/' + moment().format('YYYY-MM-DD') + '/theguardian-and-books.txt', data.join('\n\n'));
})();

