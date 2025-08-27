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

Update the name of an existing style guide.
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

**style_guide_id:** `str` — The ID of the style guide.
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` — The name of the style guide.
    
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

Start a style and brand check workflow. Returns a workflow ID to use for polling results.
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

**file_upload:** `from __future__ import annotations

core.File` — See core.File for more documentation
    
</dd>
</dl>

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

Retrieve the results of a style and brand check workflow. Returns `running` or `complete` status.
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

Start a style and brand suggestion workflow. Returns a workflow ID to use for polling results.
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

**file_upload:** `from __future__ import annotations

core.File` — See core.File for more documentation
    
</dd>
</dl>

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

Retrieve the results of a style and brand suggestion workflow. Returns `running` or `complete` status.
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

Start a style and brand rewrite workflow. Returns a workflow ID to use for polling results.
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

**file_upload:** `from __future__ import annotations

core.File` — See core.File for more documentation
    
</dd>
</dl>

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

Retrieve the results of a rewrite workflow. Returns `running` or `complete` status.
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

