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
  for (let pg = 1; pg <= 10; pg++) {
    await page.goto(
      `https://www.economist.com/science-and-technology?page=${pg}`
    );

    let listSelector = [".teaser__subheadline", ".teaser__headline.teaser__headline--sc3", ".teaser__description.teaser__description--sc2"];
    for (selector of listSelector) {
      await page.waitForSelector(selector);
      let titles = await page.$$eval(
        selector,
        (links) => links.map((x) => x.innerText)
      );
      if (data.length == 0) {
        data = titles;
      }
      else {
        data = titles.map((e, i) => data[i] + '\n' + e);
      }
    }
  }
  browser.close();
  await fse.outputFile(moment().format('YYYY-MM') + '/' + moment().format('YYYY-MM-DD') + '/science-and-technology.txt', data.join('\n\n'));
})();

