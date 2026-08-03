# eGen-commerce-images

Codex plugin marketplace for ecommerce image-production skills.

This plugin includes:

- `egen-commerce-images`: ecommerce product image strategy, localized listing copy, and GPT Image 2 prompt workflows.
- `seo-naming`: SEO-friendly ecommerce product image filename organization.

## Install From Terminal

Add this GitHub repository as a Codex plugin marketplace:

```powershell
codex plugin marketplace add https://github.com/eeeGen/egen-commerce-images
```

Install the plugin:

```powershell
codex plugin add egen-commerce-images@egen-commerce-images-marketplace
```

After installation, start a new Codex turn/session so the bundled skills are loaded.

## Update From Terminal

Refresh the marketplace snapshot:

```powershell
codex plugin marketplace upgrade egen-commerce-images-marketplace
```

Then reinstall or add the plugin again if Codex asks you to refresh the installed package:

```powershell
codex plugin add egen-commerce-images@egen-commerce-images-marketplace
```

## Repository Layout

```text
.agents/plugins/marketplace.json
plugins/egen-commerce-images/.codex-plugin/plugin.json
plugins/egen-commerce-images/skills/egen-commerce-images/SKILL.md
plugins/egen-commerce-images/skills/seo-naming/SKILL.md
```

## Direct Skill Install Fallback

If you only want the main skill without the plugin wrapper, use Codex in-session skill installer:

```text
$skill-installer install https://github.com/eeeGen/egen-commerce-images/tree/main/plugins/egen-commerce-images/skills/egen-commerce-images
```
