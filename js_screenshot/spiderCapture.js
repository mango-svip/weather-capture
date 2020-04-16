const puppeteer = require('puppeteer')

async function screenShot(url, path, name) {
    const browser = await puppeteer.launch();
    const page = await browser.newPage();
    await page.goto(url);
    await page.setViewport({
        width: 1200,
        height: 800
    });
    await page.screenshot({ path: path + name + '.png', fullPage: true });
    await browser.close();

}

(async() => {

    process.stdin.setDefaultEncoding('utf8');
    process.stdin.on('readable', () => {
        let chunk;
        while ((chunk = process.stdin.read()) !== null) {

            let url = chunk.toString("utf-8")
            if (url.indexOf("http") >= 0) {
                (async() => {
                    await screenShot(url, "", "1")
                    console.log("截图完成")
                })()

            } else {
                console.log("输入地址有误")
            }

        }
    });


})()