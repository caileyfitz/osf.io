<li node_id="${summary['id']}" class="project list-group-item list-group-item-node">
    <h4 class="list-group-item-heading">
        <span style="display:inline-block">
        <a href="${summary['url']}">${summary['title']}</a>
        % if summary['is_registration']:
            | Registered: ${summary['registered_date']}
        % endif
        </span>
        % if summary['show_logs']:
            <i id="icon-${summary['id']}" class="icon-plus pull-right" onclick="NodeActions.openCloseNode('${summary['id']}');"></i>
        % endif
    </h4>
    <div class="list-group-item-text"></div>

    <!-- Show abbreviated contributors list -->
    % if summary['show_contributors']:
        <div mod-meta='{
                "tpl": "util/render_users_abbrev.mako",
                "uri": "${summary['api_url']}contributors_abbrev/",
                "kwargs": {
                    "node_url": "${summary['url']}"
                },
                "replace": true
            }'>
        </div>
    % else:
        <span>Contributors unavailable</span>
    % endif

    % if summary['show_logs']:
        <!--Stacked bar to visualize user activity level against total activity level of a project -->
        <!--Length of the stacked bar is normalized over all projects -->
        <div class="user-activity-meter">
            <ul class="meter-wrapper">
                <li class="ua-meter" data-toggle="tooltip" title="${user_full_name} made ${summary['ua_count']} contributions" style="width:${summary['ua']}px;"></li>
                <li class="pa-meter" style="width:${summary['non_ua']}px;"></li>
                <li class="pa-meter-label">${summary['nlogs']} contributions</li>
            </ul>
        </div>

        <div class="body hide" id="body-${summary['id']}" style="overflow:hidden;">
            <hr>
            Recent Activity
            <div id="logs-${summary['id']}" class="log-container" data-uri="${summary['url']}log/"></div>
        </div>

    % endif

</li>