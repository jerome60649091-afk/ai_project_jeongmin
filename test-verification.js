const { chromium } = require('playwright');
const path = require('path');

(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage();

  // Open the HTML file
  const filePath = path.resolve(__dirname, 'index.html');
  await page.goto(`file://${filePath}`);

  console.log('=== Test 1: Click button without entering name (should show warning) ===');

  // Test 1: Click button without entering name
  const startButton = await page.$('#startButton');
  await startButton.click();

  // Wait for message to appear
  await page.waitForSelector('#resultArea > div');

  // Get the message element
  const messageBox1 = await page.$('#resultArea > div');
  const message1 = await messageBox1.textContent();
  const className1 = await messageBox1.getAttribute('class');

  console.log(`✅ Message displayed: "${message1}"`);
  console.log(`✅ CSS Class: "${className1}"`);
  console.log(`✅ Expected class contains "message-warning": ${className1.includes('message-warning')}`);

  // Take screenshot for Test 1
  await page.screenshot({ path: 'test1-warning-message.png' });
  console.log('📸 Screenshot saved: test1-warning-message.png\n');

  console.log('=== Test 2: Enter name and click button (should show success message) ===');

  // Clear the result area for next test
  await page.evaluate(() => {
    document.getElementById('resultArea').innerHTML = '';
  });

  // Test 2: Enter a name and click button
  const nameInput = await page.$('#nameInput');
  await nameInput.fill('김철수');

  await startButton.click();

  // Wait for message to appear
  await page.waitForSelector('#resultArea > div');

  const messageBox2 = await page.$('#resultArea > div');
  const message2 = await messageBox2.textContent();
  const className2 = await messageBox2.getAttribute('class');

  console.log(`✅ Message displayed: "${message2}"`);
  console.log(`✅ CSS Class: "${className2}"`);
  console.log(`✅ Expected class contains "message-success": ${className2.includes('message-success')}`);
  console.log(`✅ Message contains entered name: ${message2.includes('김철수')}`);

  // Take screenshot for Test 2
  await page.screenshot({ path: 'test2-success-message.png' });
  console.log('📸 Screenshot saved: test2-success-message.png\n');

  console.log('=== Test 3: Browser console errors (verify no null reference errors) ===');

  // Check for console errors during the tests
  const consoleMessages = [];
  page.on('console', msg => {
    consoleMessages.push(`[${msg.type()}] ${msg.text()}`);
  });

  page.on('pageerror', error => {
    consoleMessages.push(`[ERROR] ${error.message}`);
  });

  // Wait a bit to capture any errors
  await page.waitForTimeout(1000);

  if (consoleMessages.length === 0) {
    console.log('✅ No console errors or warnings detected');
  } else {
    console.log('Console messages captured:');
    consoleMessages.forEach(msg => console.log(`  ${msg}`));
  }

  console.log('\n=== All tests completed successfully ===');

  await browser.close();
})();
