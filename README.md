# Python-Web-Crawler
数据采集与网络爬虫

### HTTP响应状态码
<table>
  <th>信息性状态码</th>
  <tr><td>100</td> <td>continue</td></tr>
  <tr><td>100</td> <td>('continue')</td></tr>
  <tr><td>101</td> <td>('switching_protocols')</td></tr>
  <tr><td>102</td> <td>('processing',),</td></tr>
  <tr><td>103</td> <td>('checkpoint',),</td></tr>
  <tr><td>122</td> <td>('uri_too_long', 'request_uri_too_long'),</td></tr>

  <th>成功状态码</th>
  <tr><td>200</td> <td>('ok', 'okay', 'all_ok', 'all_okay', 'all_good', '\\o/', '✓'),</td></tr>
  <tr><td>201</td> <td>('created',),</td></tr>
  <tr><td>202</td> <td>('accepted',),</td></tr>
  <tr><td>203</td> <td>('non_authoritative_info', 'non_authoritative_information'),</td></tr>
  <tr><td>204</td> <td>('no_content',),</td></tr>
  <tr><td>205</td> <td>('reset_content', 'reset'),</td></tr>
  <tr><td>206</td> <td>('partial_content', 'partial'),</td></tr>
  <tr><td>207</td> <td>('multi_status', 'multiple_status', 'multi_stati', 'multiple_stati'),</td></tr>
  <tr><td>208</td> <td>('already_reported',),</td></tr>
  <tr><td>226</td> <td>('im_used',),</td></tr>

  <th>重定向状态码</th>
  <tr><td>300</td> <td>('multiple_choices',),</td></tr>
  <tr><td>301</td> <td>('moved_permanently', 'moved', '\\o-'),</td></tr>
  <tr><td>302</td> <td>('found',),</td></tr>
  <tr><td>303</td> <td>('see_other', 'other'),</td></tr>
  <tr><td>304</td> <td>('not_modified',),</td></tr>
  <tr><td>305</td> <td>('use_proxy',),</td></tr>
  <tr><td>306</td> <td>('switch_proxy',),</td></tr>
  <tr><td>307</td> <td>('temporary_redirect', 'temporary_moved', 'temporary'),</td></tr>
  <tr><td>308</td> <td>('permanent_redirect', 'resume_incomplete', 'resume'</td></tr>

  <th>客户端错误状态码</th>
  <tr><td>400</td> <td>('bad_request', 'bad'),</td></tr>
  <tr><td>401</td> <td>('unauthorized',),</td></tr>
  <tr><td>402</td> <td>('payment_required', 'payment'),</td></tr>
  <tr><td>403</td> <td>('forbidden',),</td></tr>
  <tr><td>404</td> <td>('not_found', '-o-'),</td></tr>
  <tr><td>405</td> <td>('method_not_allowed', 'not_allowed'),</td></tr>
  <tr><td>406</td> <td>('not_acceptable',),</td></tr>
  <tr><td>407</td> <td>('proxy_authentication_required', 'proxy_auth', 'proxy_authentication'),</td></tr>
  <tr><td>408</td> <td>('request_timeout', 'timeout'),</td></tr>
  <tr><td>409</td> <td>('conflict',),</td></tr>
  <tr><td>410</td> <td>('gone',),</td></tr>
  <tr><td>411</td> <td>('length_required',),</td></tr>
  <tr><td>412</td> <td>('precondition_failed', 'precondition'),</td></tr>
  <tr><td>413</td> <td>('request_entity_too_large',),</td></tr>
  <tr><td>414</td> <td>('request_uri_too_large',),</td></tr>
  <tr><td>415</td> <td>('unsupported_media_type', 'unsupported_media', 'media_type'),</td></tr>
  <tr><td>416</td> <td>('requested_range_not_satisfiable', 'requested_range', 'range_not_satisfiable'),</td></tr>
  <tr><td>417</td> <td>('expectation_failed',),</td></tr>
  <tr><td>418</td> <td>('im_a_teapot', 'teapot', 'i_am_a_teapot'),</td></tr>
  <tr><td>421</td> <td>('misdirected_request',),</td></tr>
  <tr><td>422</td> <td>('unprocessable_entity', 'unprocessable'),</td></tr>
  <tr><td>423</td> <td>('locked',),</td></tr>
  <tr><td>424</td> <td>('failed_dependency', 'dependency'),</td></tr>
  <tr><td>425</td> <td>('unordered_collection', 'unordered'),</td></tr>
  <tr><td>426</td> <td>('upgrade_required', 'upgrade'),</td></tr>
  <tr><td>428</td> <td>('precondition_required', 'precondition'),</td></tr>
  <tr><td>429</td> <td>('too_many_requests', 'too_many'),</td></tr>
  <tr><td>431</td> <td>('header_fields_too_large', 'fields_too_large'),</td></tr>
  <tr><td>444</td> <td>('no_response', 'none'),</td></tr>
  <tr><td>449</td> <td>('retry_with', 'retry'),</td></tr>
  <tr><td>450</td> <td>('blocked_by_windows_parental_controls', 'parental_controls'),</td></tr>
  <tr><td>451</td> <td>('unavailable_for_legal_reasons', 'legal_reasons'),</td></tr>
  <tr><td>499</td> <td>('client_closed_request',),</td></tr>

  <th>服务端错误状态码</th>
  <tr><td>500</td> <td>('internal_server_error', 'server_error', '/o\\', '✗'),</td></tr>
  <tr><td>501</td> <td>('not_implemented',),</td></tr>
  <tr><td>502</td> <td>('bad_gateway',),</td></tr>
  <tr><td>503</td> <td>('service_unavailable', 'unavailable'),</td></tr>
  <tr><td>504</td> <td>('gateway_timeout',),</td></tr>
  <tr><td>505</td> <td>('http_version_not_supported', 'http_version'),</td></tr>
  <tr><td>506</td> <td>('variant_also_negotiates',),</td></tr>
  <tr><td>507</td> <td>('insufficient_storage',),</td></tr>
  <tr><td>509</td> <td>('bandwidth_limit_exceeded', 'bandwidth'),</td></tr>
  <tr><td>510</td> <td>('not_extended',),</td></tr>
  <tr><td>511</td> <td>('network_authentication_required', 'network_auth', 'network_authentication')</td></tr>
</table>