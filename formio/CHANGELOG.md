# Changelog

## 17.0.4.0.0

Technical/API change for the `formio.form` methods `_after_create` and `_after_write`:
- Removed the `vals` argument because the respective caller methods `create` and `write` raised a Singleton Error upon `copy`.\
  This also simplifies the `create` and `write` methods.
- Call the `_process_api_components` method per record iteration.

## 17.0.3.4.0

- Add Form Builder setting (boolean field) to display a Form in "full width" 100% or 75%.
- Changed the default width of a Form to 75%.

## 17.0.3.3.0

Add descriptions with recommended modules in the `formio.builder.js.options` data.

## 17.0.3.2.0

Improve the Form Builder and Form button styling (colors).

## 17.0.3.1.0

Improvements for the `formio.builder.js.options`:
- Add a wizard to merge other `formio.builder.js.options` record field `value`.
- Add default and tracking for `formio.builder.js.options` field `value`.

Add a utils function `json_loads()`:\
Refactored the `try/except` with `json.loads()` and `ast.literal_eval()` calls, to use the utils `json_loads()` function.

## 17.0.3.0.0

Improvements and migration for the `formio.builder.js.options`:
- Add `editForm` components and options in `formio_builder_js_options_default`.
- Change `formio_builder_js_options_default` storage from Python Dict to JSON notation/syntax.
- Migrate `formio.builder` records (field) `formio_js_options` to merge the updated `formio_builder_js_options_default`.
- Migrate `formio.builder.js.options.default` records to merge the updated `formio_builder_js_options_default`.
- Improve the "Form Builder formio.js Options" form view (`view_formio_builder_js_options_form`): Add `widget='ace'` (`mode: js`).

## 17.0.2.0.1

- Fix migration scipts to support big jumps/leaps without crashing due to non-existent fields.
- Form Builder: Add badge "Locked Disabled".

## 17.0.2.0.0

Rename and migrate Form Builder field `public_uuid` to `current_uuid`.\
The `current_uuid` is a more meaningful name.

## 17.0.1.8.0

In Form Builder views (list, form, search) add:
- Field Public UUID (`public_uuid`)
- Public Current URL (`public_current_url`)

This is in addition to version 17.0.1.5.

## 17.0.1.7.0

Migrate the Form Builder (`formio.builder`) field `submission_url_add_query_params_from` to endpoint specific fields:
- `portal_submission_url_add_query_params_from`
- `portal_submission_url_add_query_params_from`
- `backend_submission_url_add_query_params_from`

This makes it possible to distinguish the setting per endpoint.

## 17.0.1.6.0

Minor form builder view migration fix (column_invisible).

## 17.0.1.5.0

### Allow (support) versioning for publicly published forms (form builders)

Add endpoint `/formio/public/form/new/current/<string:builder_public_uuid>` that allows to update the form builders (versioning) and keep them published when the state is "Current".\
This required to add the `formio.builder` model field `public_uuid`, that is identical to all `formio.builder` records with the same name.

## 17.0.1.4.0

In the Form Builder, show a "Locked" badge in case it is locked.

## 17.0.1.3.0

Add new group "Forms: Allow updating form submission data".\
Users in this group are allowed to edit and update the (raw, JSON) submission data in the `formio.form` form view.

## 17.0.1.2.0

- Fix formioScrollIntoView event handler.
- Default value for form builder fields: `portal_scroll_into_view`, `public_scroll_into_view`

## 17.0.1.1.0

Improve the formio.js library registration (downloader, importer) with a new setting to allow only registered versions.\
This adds a new system parameter `ir.config_parameter` which currently defaults to 'v4' and can be modified in the configuration window.\
The allowed setting is a comma separated string (list) of formio.js versions to register. Examples:
- v4,v5
- v4.17,v4.18

## 17.0.1.0.0

Initial release.