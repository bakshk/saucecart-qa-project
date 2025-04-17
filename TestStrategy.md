# Test Strategy – SauceCart QA Project

## Objective
To ensure the core functionalities of the SauceDemo e-commerce app (login, cart, checkout) are tested thoroughly using a combination of manual and automated testing approaches.

## Scope
- Functional Testing
- Integration Testing
- End-to-End Testing
- UI/UX Validation
- Bug Reporting

## Out of Scope
- Load/Performance Testing
- Payment Gateway (as it’s a demo site)

## Testing Types
- Manual Testing for UI, error handling, field validation
- Automation Testing using Selenium WebDriver (login and checkout)

## Test Environment
- Browser: Chrome (primary), Firefox (secondary)
- Platform: SauceDemo – [https://www.saucedemo.com/](https://www.saucedemo.com/)

## Tools Used
- Google Docs & Sheets (for test cases and reporting)
- Selenium + Python (for automation)
- GitHub (version control & documentation)

## Risk & Mitigation
| Risk | Mitigation |
|------|------------|
| Demo app instability | Retest as needed, retry with backups |
| Limited scope for real transactions | Focus on flow, not live payments |
