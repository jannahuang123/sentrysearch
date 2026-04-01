# SentrySearch Landing Page Design

Date: 2026-04-01
Topic: SentrySearch term-definition landing page with sample search demo

## Goal

Launch a fast, indexable landing page that helps search engines and users understand `SentrySearch` as a new term meaning:

> Search dashcam and security footage with natural language, then automatically trim the matching clip.

This page is meant to win early rankings for the new word `SentrySearch`, while also capturing adjacent intent such as:

- `search dashcam footage`
- `natural language video search`
- `search security video`
- `auto trim clip from video`

The first release should prioritize semantic clarity, crawlability, and trust over product complexity.

## Product Positioning

`SentrySearch` should be presented as a concrete utility, not as a vague AI platform.

The page should define the term directly, then immediately prove its value with realistic search scenarios from dashcam and security footage. The narrative should stay grounded in the repository's real capability: local or self-run natural language search over video, with clip extraction from matched results.

The page should not imply that users can already upload private videos to a hosted web app. That would create a product expectation mismatch with the current repository.

## Primary Audience

The landing page is for three overlapping audiences:

1. People who encounter the word `SentrySearch` directly and want to know what it means.
2. People searching for a way to find incidents inside dashcam or security footage.
3. People willing to try a local/open-source workflow if the value is clear and immediate.

## Success Criteria

The design is successful if the page does the following:

- Makes the meaning of `SentrySearch` obvious within the first screen.
- Associates `SentrySearch` with natural language search for dashcam and security video.
- Demonstrates the "search, find, trim" workflow without requiring real upload infrastructure.
- Creates a believable path to action through GitHub and a secondary hosted-interest CTA.
- Leaves room for a later hosted product without overpromising it now.

## Page Strategy

The recommended approach is a hybrid of:

- term-definition page
- problem-solving page
- scenario-driven product page

The page should first define the word `SentrySearch`, then immediately anchor it in real user jobs such as finding a close call, driveway event, or suspicious moment from many hours of footage.

This structure balances brand-term capture with higher-intent long-tail discovery.

## Messaging Hierarchy

The page should communicate the following hierarchy in order:

1. `SentrySearch` is a specific thing.
2. That thing lets you describe an event in plain English.
3. It finds the right moment inside dashcam or security footage.
4. It automatically trims the matching clip.
5. You can try the concept through a sample demo now and run the real tool locally.

## Information Architecture

The page should include these sections in this order.

### 1. Hero

Purpose: define the term and communicate the full promise immediately.

Required content:

- H1 containing `SentrySearch` and the complete function
- short supporting sentence emphasizing natural language search plus auto-trimmed output
- primary CTA: sample search demo
- secondary CTA: GitHub repository

Example direction:

- H1: `SentrySearch: Search Dashcam and Security Video with Natural Language`
- supporting copy: `Describe what happened, find the right moment, and automatically trim the matching clip.`

### 2. Definition Block

Purpose: explicitly answer "What is SentrySearch?"

This section should define the term in plain language with 2 to 3 short paragraphs or equivalent concise copy. It should make it easy for search engines and readers to map the new word to a clear category.

### 3. Use Cases

Purpose: prove relevance with realistic search intent.

Use cards or short rows for representative queries such as:

- `Find the moment a car cut in front of me`
- `Find when someone approached the driveway`
- `Find the clip with a red truck near the stop sign`
- `Find the moment a car door ding happened`

These examples should look like real things users would type, not sanitized demo prompts.

### 4. Sample Search Demo

Purpose: simulate product value without building hosted upload and inference.

This section should provide a front-end-only interactive demo with preloaded example queries and precomputed result states. The interaction should feel like a real search workflow:

- user selects or enters a sample query
- page displays matching clip result(s)
- each result includes source name, timestamp, confidence-style score, and trimmed clip outcome

Optional media:

- a short demo video
- static result previews
- animated state changes when a sample query is run

### 5. How It Works

Purpose: explain the mechanism in an honest, simplified flow.

Use a clear 3-step model:

1. Index footage
2. Search in plain English
3. Get the matching clip

This section should stay concrete and avoid abstract AI language.

### 6. FAQ

Purpose: capture long-tail search intent and remove ambiguity.

Recommended questions:

- `What is SentrySearch?`
- `Can SentrySearch search dashcam footage?`
- `Can it search security camera footage too?`
- `Does SentrySearch upload my videos?`
- `Can I run SentrySearch locally?`
- `Is this a Tesla Sentry Mode tool only?`

### 7. Final CTA

Purpose: convert without overpromising.

Recommended CTA pair:

- primary: `Run locally today`
- secondary: `Request hosted demo`

The hosted/demo CTA should be present but visually secondary so users understand it is not the main current product path.

## SEO Requirements

The implementation should include:

- unique page title with `SentrySearch` near the front
- meta description focused on natural language video search and clip trimming
- canonical URL
- Open Graph title and description
- descriptive heading structure with a single H1
- crawlable text for all key claims

Suggested primary keyword:

- `SentrySearch`

Suggested support keywords:

- `search dashcam footage`
- `search security video`
- `natural language video search`
- `AI video search`
- `trim clip from video`

The page should remain centered on the invented term `SentrySearch`, rather than becoming a generic AI video landing page.

## Demo Boundaries

The sample demo must stay inside these boundaries:

- no real user video upload
- no backend inference
- no storage or account system
- no promise that private footage can already be processed in the browser

The sample interaction should be framed as a product demonstration, not as full hosted functionality.

## Visual and Copy Direction

The tone should be practical, confident, and direct.

Avoid:

- inflated AI-marketing language
- enterprise platform jargon
- generic productivity framing

Prefer:

- event-focused wording
- concrete video search examples
- language that sounds useful when read from a search result

The design should feel modern and intentional, but the visual system should support comprehension first. This is a definition page with product proof, not a decorative brand campaign.

## Visual Direction Update

After reviewing visual references in `stitch/`, the approved visual direction is no longer a light Product Hunt-style SaaS page. The landing page should instead move closer to a dark, night-dashboard product style while remaining a marketing homepage rather than a full application shell.

Approved direction:

- dark landing page with strong product-control-panel energy
- closer to a serious video operations dashboard than a generic SaaS template
- visually aligned with the "dashboard at night" feel from the `stitch/` references
- product-first, not AI-first

This update replaces the earlier assumption of a bright, airy SaaS landing page.

## Hero Visual System

The hero should use a two-column structure:

- left side: concise headline, support copy, and primary CTA pair
- right side: a polished product panel that looks like a real incident-search interface

The right-side panel should show product evidence, not abstract decoration. It should include some combination of:

- a realistic query
- a matched clip card
- clip range or timestamp range
- confidence or match quality signal
- camera/source metadata
- clip saved/exported state

The visual should feel like a premium control surface, not an illustration.

## Image Strategy Update

The approved image system is:

- product UI plus real-world scenes

This means the page should combine interface-driven visuals with realistic dashcam/security imagery. It should not rely on stock-photo-heavy lifestyle marketing, and it should not use abstract AI art.

Recommended visual assets:

- one primary product mockup or control-panel composition in the hero
- two or three supporting visual cards tied to concrete event scenarios
- real-world scene backplates for dashcam, parking lot, or driveway moments

Every visual should reinforce the core action:

1. describe the incident
2. locate the right moment
3. save the matching clip

## Scene Prioritization

The primary market-facing scenario should be dashcam and driving incidents.

The page should lead with examples such as:

- a car cutting in front
- a parking lot incident
- a near miss at an intersection

Security-footage scenarios should still appear, but as secondary expansion use cases rather than the first visual story.

## Layout Personality

The page should preserve landing-page clarity while borrowing the best aspects of application UI:

- strong sectional framing
- compact metadata chips and labels
- result cards with state indicators
- restrained, high-contrast palette
- subtle lighting and surface depth

Avoid turning the page into a fake full dashboard with heavy navigation chrome or too many app-like controls. The visitor should still understand immediately that this is a homepage.

## Color And Typography Direction

The palette should be dark and restrained:

- deep navy, obsidian, slate, and muted steel tones
- restrained blue/teal highlights for active states
- high-contrast text with muted support copy

Typography should feel more premium and product-grade than generic startup marketing. The page should read like serious software, not a playful AI tool.

## Copy Direction Update

The copy should be less "AI landing page" and more "serious incident retrieval product."

Prefer wording around:

- incidents
- footage
- matched clips
- saved evidence
- exact moments
- incident review

De-emphasize language around:

- AI magic
- automation hype
- generic platform claims

## Implementation Impact

Any future visual implementation should treat the current landing page as functionally correct but stylistically provisional.

The next implementation phase should focus on:

- reworking the page into the approved dark visual system
- replacing the current light SaaS styling
- introducing product-panel compositions and scene-backed visuals
- preserving all existing product boundaries, copy constraints, CTA intent, and demo-only behavior

## Non-Goals

The first release should explicitly avoid:

- hosted video upload
- real-time web search over private footage
- authentication
- billing
- multi-user dashboards
- broad "AI platform" positioning

These may become future expansions, but they are outside the scope of the first landing page.

## Future-Compatible Extension Path

The design should leave room for a later hosted product by preserving space for:

- hosted demo request capture
- waitlist or early access CTA
- future replacement of the sample demo with real uploaded demo footage

However, none of these future states should shape the first-release promise more than the current product reality.

## Implementation Scope For Version 1

Version 1 should include:

- one standalone landing page
- complete copy for hero, definition, use cases, how-it-works, FAQ, and CTAs
- a front-end-only sample search demo
- metadata for SEO and social sharing
- direct GitHub CTA

Version 1 should not include:

- hosted search backend
- user uploads
- user accounts
- real indexing jobs
- a false "try your own video" experience

## Core Sentence

The single sentence the page must make unforgettable is:

`SentrySearch lets you search dashcam and security footage in natural language and automatically trim the matching clip.`
