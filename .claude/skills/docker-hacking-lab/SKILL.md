```markdown
# docker-hacking-lab Development Patterns

> Auto-generated skill from repository analysis

## Overview

This skill covers the core development patterns and workflows for the `docker-hacking-lab` repository. The project is written in TypeScript and focuses on building and maintaining a container security course, including the creation and management of multi-format training modules and documentation. The repository emphasizes consistency in file naming, import/export styles, and supports collaborative workflows for adding new course content and documentation.

## Coding Conventions

### File Naming

- Use **snake_case** for all filenames.
  - Example: `module_summary_script.md`, `video_01_script.docx`

### Import Style

- Use **relative imports** for all TypeScript modules.
  - Example:
    ```typescript
    import { getModuleData } from './module_utils';
    ```

### Export Style

- Use **named exports** for functions, constants, and types.
  - Example:
    ```typescript
    // module_utils.ts
    export function getModuleData() { ... }
    export const MODULE_VERSION = '1.0';
    ```

### Commit Messages

- Freeform style, no enforced prefixes.
- Typical length: ~63 characters.

## Workflows

### Add New Course Module

**Trigger:** When someone wants to add a new training module to the course.  
**Command:** `/new-course-module`

1. Create a new directory under `container-security-course/` with a descriptive name (e.g., `module_01_fundamentals`).
2. Add video scripts for each topic in the module in `.md`, `.docx`, and `.pdf` formats.
   - Example:
     ```
     container-security-course/module_01_fundamentals/video_01_script.md
     container-security-course/module_01_fundamentals/video_01_script.docx
     container-security-course/module_01_fundamentals/video_01_script.pdf
     ```
3. Add a module summary script in `.md`, `.docx`, and `.pdf` formats.
   - Example:
     ```
     container-security-course/module_01_fundamentals/module_summary_script.md
     ```
4. Add questions for the module in `.md`, `.docx`, and `.pdf` formats.
   - Example:
     ```
     container-security-course/module_01_fundamentals/questions.md
     ```
5. Add metadata for the module in `.md`, `.docx`, and `.pdf` formats.
   - Example:
     ```
     container-security-course/module_01_fundamentals/metadata.md
     ```

**Tip:** Maintain consistent naming and file structure for all modules.

---

### Add Multiformat Course Document

**Trigger:** When someone wants to add or update general course documentation in all supported formats.  
**Command:** `/add-course-doc`

1. Create or update the document in Markdown (`.md`).
   - Example: `container-security-course/course_outline.md`
2. Convert or export the document to DOCX (`.docx`).
   - Example: `container-security-course/course_outline.docx`
3. Convert or export the document to PDF (`.pdf`).
   - Example: `container-security-course/course_outline.pdf`
4. For summaries, optionally add HTML (`.html`) format.
   - Example: `container-security-course/course_summary.html`

**Tip:** Ensure all formats are updated together to keep content in sync.

## Testing Patterns

- **Framework:** Not explicitly specified.
- **Test File Pattern:** Files matching `*.test.*` (e.g., `module_utils.test.ts`).
- **Location:** Test files are typically placed alongside the code they test.
- **Example:**
  ```typescript
  // module_utils.test.ts
  import { getModuleData } from './module_utils';

  test('getModuleData returns correct structure', () => {
    // ...test logic...
  });
  ```

## Commands

| Command             | Purpose                                                        |
|---------------------|----------------------------------------------------------------|
| /new-course-module  | Add a new module to the container security course              |
| /add-course-doc     | Add or update course-wide documentation in all supported formats|
```
