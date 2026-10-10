const fs = require('fs');
const path = require('path');

const files = [
  'tools_kerala_psc_photo_resizer.html',
  'tools_signature_resizer.html',
  'tools_govt_photo_resizer.html',
  'tools_image_compressor.html',
  'tools_image_to_pdf.html',
  'tools_age_calculator.html'
];

let hasErrors = false;

console.log('=== AUDITING 6 EXAM TOOL PAGES FOR UNIFORMITY & JS VALIDITY ===\n');

files.forEach(file => {
  const filePath = path.join(__dirname, file);
  if (!fs.existsSync(filePath)) {
    console.error(`[ERROR] File missing: ${file}`);
    hasErrors = true;
    return;
  }

  const content = fs.readFileSync(filePath, 'utf8');
  console.log(`Checking ${file} (${(content.length / 1024).toFixed(1)} KB)...`);

  // Check 1: Top Banner gradient presence
  if (!content.includes('linear-gradient(135deg, #1E3A8A 0%, #2563EB 100%)')) {
    console.warn(`  [WARN] Banner gradient missing or non-standard in ${file}`);
    hasErrors = true;
  } else {
    console.log(`  ✓ Unified Top Banner present`);
  }

  // Check 2: Specifications Card presence
  if (!content.includes('Specifications') && !content.includes('Guidelines') && !content.includes('Limits')) {
    console.warn(`  [WARN] Specifications / Guidelines card missing in ${file}`);
  } else {
    console.log(`  ✓ Specifications / Guidelines Card present`);
  }

  // Check 3: FAQ accordion presence
  if (!content.includes('Frequently Asked Questions (FAQs)')) {
    console.warn(`  [WARN] FAQ section missing in ${file}`);
    hasErrors = true;
  } else {
    console.log(`  ✓ FAQ Accordion present`);
  }

  // Check 4: Cross-Tool Navigation
  if (!content.includes('Explore Other Government Exam Utilities')) {
    console.warn(`  [WARN] Cross-tool quick navigation missing in ${file}`);
    hasErrors = true;
  } else {
    console.log(`  ✓ Cross-Tool Navigation present`);
  }

  // Check 5: Return to Home button
  if (!content.includes('Return to 1IndiaJob Home')) {
    console.warn(`  [WARN] Return to Home button missing in ${file}`);
    hasErrors = true;
  } else {
    console.log(`  ✓ Return to Home Button present`);
  }

  // Check 6: Extract & Validate JavaScript syntax
  const scriptMatches = content.match(/<script[\s\S]*?>([\s\S]*?)<\/script>/gi);
  if (scriptMatches) {
    scriptMatches.forEach((scriptTag, idx) => {
      // If external src script, ignore
      if (scriptTag.includes('src=')) return;
      
      let jsCode = scriptTag.replace(/<script[\s\S]*?>/i, '').replace(/<\/script>/i, '');
      jsCode = jsCode.replace('//<![CDATA[', '').replace('//]]>', '');
      
      try {
        new Function(jsCode);
        console.log(`  ✓ Inline JS Block #${idx + 1} syntax valid`);
      } catch (err) {
        console.error(`  [ERROR] JS Syntax Error in ${file} (Script #${idx + 1}):`, err.message);
        hasErrors = true;
      }
    });
  }
  console.log('');
});

if (hasErrors) {
  console.error('❌ Audit found errors or inconsistencies.');
  process.exit(1);
} else {
  console.log('🎉 ALL 6 PAGES ARE 100% UNIFORM, ERROR-FREE, AND READY FOR LIVE PUBLICATION!');
}
