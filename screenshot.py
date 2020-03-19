import pyppeteer
import asyncio
import time

async def _init():
    browser = await pyppeteer.launch({'headless': False,
                                    # 'userDataDir': './userdata',
                                    'args': [
                                        # '--window-size={800},{600}'
                                        '--disable-extensions',
                                        '--user-agent=iPhone X',
                                        # '--hide-scrollbars',
                                        '--disable-bundled-ppapi-flash',
                                        '--mute-audio',
                                        '--no-sandbox',
                                        '--disable-setuid-sandbox',
                                        '--disable-gpu',
                                        '--disable-infobars'
                                    ],
                                    'dumpio': False
                                    })
    page = await browser.newPage()
    await page.setUserAgent('Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1')
    #iphone x size 
    await page.setViewport({'width': 414, 'height': 896})
    # await page.goto('https://m.weather.com.cn/tips/index.html?aid=101020200')
    
    await getWeather(page, '上海天气预报', 'today.png')

    await getWeather(page, '北京天气预报', 'bj.png')

    # time.sleep(1000000)

async def getWeather(page, location, imageName):
    await page.goto('https://www.baidu.com/s?wd=' + location)
    btn = await page.querySelector('.c-span3')
    # time.sleep(1000000)
    await btn.click()
    res = await page.querySelector('.c-result-content')
    await screen(res, imageName)

async def screen(element, imageName): 
    return await element.screenshot({'path': imageName, 'quality': 100, 'fullPage': False})

loop = asyncio.get_event_loop()
task = asyncio.ensure_future(_init())
loop.run_until_complete(task)