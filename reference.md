# Reference
## Style Guides
<details><summary><code>client.style_guides.<a href="src/markup_ai/style_guides/client.py">list_style_guides</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve all style guides associated with your organization.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from markup_ai import MarkupAI

client = MarkupAI(
    token="YOUR_TOKEN",
)
client.style_guides.list_style_guides()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.style_guides.<a href="src/markup_ai/style_guides/client.py">create_style_guide</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new style guide that can be used in checks, suggestions, and rewrites.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from markup_ai import MarkupAI

client = MarkupAI(
    token="YOUR_TOKEN",
)
client.style_guides.create_style_guide(
    name="name",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**file_upload:** `from __future__ import annotations

core.File` — See core.File for more documentation
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` — A friendly name for your style guide to help you identify it later.
    
</dd>
</dl>

<dl>
<dd>

**base_style_guide:** `typing.Optional[BaseStyleGuideType]` — The base style guide to extend (AP, Chicago, or Microsoft). If not provided, the style guide will be created from scratch.
    
</dd>
</dl>

<dl>
<dd>

**terminology_domain_ids:** `typing.Optional[typing.List[str]]` — List of domain IDs to filter terminology searches by. NULL or empty list means no filtering.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.style_guides.<a href="src/markup_ai/style_guides/client.py">get_style_guide</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve a specific style guide by ID, including its metadata such as `name` and `status`.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from markup_ai import MarkupAI

client = MarkupAI(
    token="YOUR_TOKEN",
)
client.style_guides.get_style_guide(
    style_guide_id="style_guide_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**style_guide_id:** `str` — The ID of the style guide.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.style_guides.<a href="src/markup_ai/style_guides/client.py">delete_style_guide</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete a style guide by ID.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from markup_ai import MarkupAI

client = MarkupAI(
    token="YOUR_TOKEN",
)
client.style_guides.delete_style_guide(
    style_guide_id="style_guide_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**style_guide_id:** `str` — The ID of the style guide.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.style_guides.<a href="src/markup_ai/style_guides/client.py">update_style_guide</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update the name and/or terminology domain IDs of an existing style guide.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from markup_ai import MarkupAI

client = MarkupAI(
    token="YOUR_TOKEN",
)
client.style_guides.update_style_guide(
    style_guide_id="style_guide_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**style_guide_id:** `str` — The ID of the style guide.
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — The name of the style guide.
    
</dd>
</dl>

<dl>
<dd>

**terminology_domain_ids:** `typing.Optional[typing.Sequence[str]]` — List of domain IDs to filter terminology searches by. NULL or empty list means no filtering.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Style Checks
<details><summary><code>client.style_checks.<a href="src/markup_ai/style_checks/client.py">create_style_check</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Analyze text for grammar, style, and clarity issues.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from markup_ai import MarkupAI

client = MarkupAI(
    token="YOUR_TOKEN",
)
client.style_checks.create_style_check(
    dialect="american_english",
    style_guide="style_guide",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**dialect:** `Dialects` — The language variant you'd like us to use for analysis. Choose from American English, British English, or other supported dialects.
    
</dd>
</dl>

<dl>
<dd>

**style_guide:** `str` — The style guide to follow for your content. You can use a style guide ID or choose from built-in options: `ap`, `chicago`, or `microsoft`.
    
</dd>
</dl>

<dl>
<dd>

**file_upload:** `from __future__ import annotations

core.File` — See core.File for more documentation
    
</dd>
</dl>

<dl>
<dd>

**tone:** `typing.Optional[Tones]` — The tone variation you're aiming for. Options include formal, academic, casual, and other tone variations to match your content goals.
    
</dd>
</dl>

<dl>
<dd>

**webhook_url:** `typing.Optional[str]` — A URL that results will be POSTed to once the process completes.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.style_checks.<a href="src/markup_ai/style_checks/client.py">get_style_check</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve style check results.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from markup_ai import MarkupAI

client = MarkupAI(
    token="YOUR_TOKEN",
)
client.style_checks.get_style_check(
    workflow_id="workflow_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**workflow_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Style Suggestions
<details><summary><code>client.style_suggestions.<a href="src/markup_ai/style_suggestions/client.py">create_style_suggestion</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get suggested corrections for text.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from markup_ai import MarkupAI

client = MarkupAI(
    token="YOUR_TOKEN",
)
client.style_suggestions.create_style_suggestion(
    dialect="american_english",
    style_guide="style_guide",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**dialect:** `Dialects` — The language variant you'd like us to use for analysis. Choose from American English, British English, or other supported dialects.
    
</dd>
</dl>

<dl>
<dd>

**style_guide:** `str` — The style guide to follow for your content. You can use a style guide ID or choose from built-in options: `ap`, `chicago`, or `microsoft`.
    
</dd>
</dl>

<dl>
<dd>

**file_upload:** `from __future__ import annotations

core.File` — See core.File for more documentation
    
</dd>
</dl>

<dl>
<dd>

**tone:** `typing.Optional[Tones]` — The tone variation you're aiming for. Options include formal, academic, casual, and other tone variations to match your content goals.
    
</dd>
</dl>

<dl>
<dd>

**webhook_url:** `typing.Optional[str]` — A URL that results will be POSTed to once the process completes.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.style_suggestions.<a href="src/markup_ai/style_suggestions/client.py">get_style_suggestion</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve suggestion results.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from markup_ai import MarkupAI

client = MarkupAI(
    token="YOUR_TOKEN",
)
client.style_suggestions.get_style_suggestion(
    workflow_id="workflow_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**workflow_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Style Rewrites
<details><summary><code>client.style_rewrites.<a href="src/markup_ai/style_rewrites/client.py">create_style_rewrite</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Rewrite text with style corrections applied.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from markup_ai import MarkupAI

client = MarkupAI(
    token="YOUR_TOKEN",
)
client.style_rewrites.create_style_rewrite(
    dialect="american_english",
    style_guide="style_guide",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**dialect:** `Dialects` — The language variant you'd like us to use for analysis. Choose from American English, British English, or other supported dialects.
    
</dd>
</dl>

<dl>
<dd>

**style_guide:** `str` — The style guide to follow for your content. You can use a style guide ID or choose from built-in options: `ap`, `chicago`, or `microsoft`.
    
</dd>
</dl>

<dl>
<dd>

**file_upload:** `from __future__ import annotations

core.File` — See core.File for more documentation
    
</dd>
</dl>

<dl>
<dd>

**tone:** `typing.Optional[Tones]` — The tone variation you're aiming for. Options include formal, academic, casual, and other tone variations to match your content goals.
    
</dd>
</dl>

<dl>
<dd>

**webhook_url:** `typing.Optional[str]` — A URL that results will be POSTed to once the process completes.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.style_rewrites.<a href="src/markup_ai/style_rewrites/client.py">get_style_rewrite</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve rewrite results.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from markup_ai import MarkupAI

client = MarkupAI(
    token="YOUR_TOKEN",
)
client.style_rewrites.get_style_rewrite(
    workflow_id="workflow_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**workflow_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Terminology
<details><summary><code>client.terminology.<a href="src/markup_ai/terminology/client.py">export_terminology</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Exports all term sets, terms and domains to CSV. The exported CSV follows the same format as the CSV import.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from markup_ai import MarkupAI

client = MarkupAI(
    token="YOUR_TOKEN",
)
client.terminology.export_terminology()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.terminology.<a href="src/markup_ai/terminology/client.py">import_terminology</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Uploads a CSV or ACTIF XML file and imports terminology.

**CSV Format Requirements:**
- CSV must include columns: Prohibited, Preferred, Context-Dependent, Instructions, Domains
- The first row must contain the column headers in the exact same order as shown above
- Multiple values within a single cell should be separated by semicolons with a space (e.g., term1; term2; term3)
- Empty cells are allowed
- The CSV import format is the same as the CSV export format.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from markup_ai import MarkupAI

client = MarkupAI(
    token="YOUR_TOKEN",
)
client.terminology.import_terminology(
    delete_existing=True,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**file:** `from __future__ import annotations

core.File` — See core.File for more documentation
    
</dd>
</dl>

<dl>
<dd>

**delete_existing:** `typing.Optional[bool]` — Delete all existing terms, term sets and domains before importing
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.terminology.<a href="src/markup_ai/terminology/client.py">search_terminology</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Searches the text for relevant terminology and returns matched term sets.

Term sets are matched if any word sequence (up to 5 words) in the text is similar to one of the terms of the term set.
The similarity measure used is a trigram similarity of 0.5 or higher between the word sequence and the term.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from markup_ai import MarkupAI

client = MarkupAI(
    token="YOUR_TOKEN",
)
client.terminology.search_terminology(
    query="query",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**query:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**domain_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Optional domain filter
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.terminology.<a href="src/markup_ai/terminology/client.py">list_term_sets</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a pageable list of term sets with all their associated terms and domains.

The search filter searches the term set instructions and term text fields.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from markup_ai import MarkupAI

client = MarkupAI(
    token="YOUR_TOKEN",
)
client.terminology.list_term_sets(
    page=1,
    page_size=1,
    search_term="search_term",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**page:** `typing.Optional[int]` — Page number (1-based)
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` — Number of items per page
    
</dd>
</dl>

<dl>
<dd>

**search_term:** `typing.Optional[str]` — Optional search term to filter term sets
    
</dd>
</dl>

<dl>
<dd>

**domain_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Optional domain filter (any of these domains)
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.terminology.<a href="src/markup_ai/terminology/client.py">create_term_set</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new term set. Terms and domains are linked to term sets.
The term set instructions text will be used to determine whether a term should be flagged in the text and what the term replacement should be.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from markup_ai import MarkupAI

client = MarkupAI(
    token="YOUR_TOKEN",
)
client.terminology.create_term_set(
    instructions="instructions",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**instructions:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**terms:** `typing.Optional[typing.Sequence[TermCreateRequest]]` 
    
</dd>
</dl>

<dl>
<dd>

**domain_ids:** `typing.Optional[typing.Sequence[str]]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.terminology.<a href="src/markup_ai/terminology/client.py">get_term_set</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from markup_ai import MarkupAI

client = MarkupAI(
    token="YOUR_TOKEN",
)
client.terminology.get_term_set(
    term_set_id="term_set_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**term_set_id:** `str` — UUID of the term set
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.terminology.<a href="src/markup_ai/terminology/client.py">delete_term_set</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from markup_ai import MarkupAI

client = MarkupAI(
    token="YOUR_TOKEN",
)
client.terminology.delete_term_set(
    term_set_id="term_set_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**term_set_id:** `str` — UUID of the term set
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.terminology.<a href="src/markup_ai/terminology/client.py">update_term_set</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from markup_ai import MarkupAI

client = MarkupAI(
    token="YOUR_TOKEN",
)
client.terminology.update_term_set(
    term_set_id="term_set_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**term_set_id:** `str` — UUID of the term set
    
</dd>
</dl>

<dl>
<dd>

**instructions:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**domain_ids:** `typing.Optional[typing.Sequence[str]]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.terminology.<a href="src/markup_ai/terminology/client.py">create_term</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create terms that should be matched in the text. The term types are:

* **preferred**: this is the preferred term for the associated term set
* **prohibited**: this term should not be used to talk about the term set
* **context_dependent**: this term is correct in certain cases, but incorrect in others, the instructions field of the term set should explain when the term is correct and when it is incorrect
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from markup_ai import MarkupAI

client = MarkupAI(
    token="YOUR_TOKEN",
)
client.terminology.create_term(
    term_set_id="term_set_id",
    term="term",
    type="preferred",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**term_set_id:** `str` — UUID of the term set
    
</dd>
</dl>

<dl>
<dd>

**term:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**type:** `TermType` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.terminology.<a href="src/markup_ai/terminology/client.py">get_term</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from markup_ai import MarkupAI

client = MarkupAI(
    token="YOUR_TOKEN",
)
client.terminology.get_term(
    term_set_id="term_set_id",
    term_id="term_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**term_set_id:** `str` — UUID of the term set
    
</dd>
</dl>

<dl>
<dd>

**term_id:** `str` — UUID of the term
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.terminology.<a href="src/markup_ai/terminology/client.py">update_term</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from markup_ai import MarkupAI

client = MarkupAI(
    token="YOUR_TOKEN",
)
client.terminology.update_term(
    term_set_id="term_set_id",
    term_id="term_id",
    term="term",
    type="preferred",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**term_set_id:** `str` — UUID of the term set
    
</dd>
</dl>

<dl>
<dd>

**term_id:** `str` — UUID of the term
    
</dd>
</dl>

<dl>
<dd>

**term:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**type:** `TermType` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.terminology.<a href="src/markup_ai/terminology/client.py">delete_term</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from markup_ai import MarkupAI

client = MarkupAI(
    token="YOUR_TOKEN",
)
client.terminology.delete_term(
    term_set_id="term_set_id",
    term_id="term_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**term_set_id:** `str` — UUID of the term set
    
</dd>
</dl>

<dl>
<dd>

**term_id:** `str` — UUID of the term
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.terminology.<a href="src/markup_ai/terminology/client.py">list_domains</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from markup_ai import MarkupAI

client = MarkupAI(
    token="YOUR_TOKEN",
)
client.terminology.list_domains(
    page=1,
    page_size=1,
    search="search",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**page:** `typing.Optional[int]` — Page number (1-based)
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` — Number of items per page
    
</dd>
</dl>

<dl>
<dd>

**search:** `typing.Optional[str]` — Optional name filter
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.terminology.<a href="src/markup_ai/terminology/client.py">create_domain</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from markup_ai import MarkupAI

client = MarkupAI(
    token="YOUR_TOKEN",
)
client.terminology.create_domain(
    name="name",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.terminology.<a href="src/markup_ai/terminology/client.py">get_domain</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from markup_ai import MarkupAI

client = MarkupAI(
    token="YOUR_TOKEN",
)
client.terminology.get_domain(
    domain_id="domain_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**domain_id:** `str` — UUID of the domain
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.terminology.<a href="src/markup_ai/terminology/client.py">delete_domain</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from markup_ai import MarkupAI

client = MarkupAI(
    token="YOUR_TOKEN",
)
client.terminology.delete_domain(
    domain_id="domain_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**domain_id:** `str` — UUID of the domain
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.terminology.<a href="src/markup_ai/terminology/client.py">update_domain</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from markup_ai import MarkupAI

client = MarkupAI(
    token="YOUR_TOKEN",
)
client.terminology.update_domain(
    domain_id="domain_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**domain_id:** `str` — UUID of the domain
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

