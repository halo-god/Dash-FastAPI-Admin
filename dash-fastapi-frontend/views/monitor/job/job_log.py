from dash import dcc, html
import feffery_antd_components as fac

import callbacks.monitor_c.job_c.job_log_c


def render(button_perms):

    return [
        dcc.Store(id='job_log-button-perms-container', data=button_perms),
        # 用于导出成功后重置dcc.Download的状态，防止多次下载文件
        dcc.Store(id='job_log-export-complete-judge-container'),
        # 绑定的导出组件
        dcc.Download(id='job_log-export-container'),
        fac.AntdRow(
            [
                fac.AntdCol(
                    [
                        fac.AntdRow(
                            [
                                fac.AntdCol(
                                    html.Div(
                                        [
                                            fac.AntdForm(
                                                [
                                                    fac.AntdFormItem(
                                                        fac.AntdInput(
                                                            id='job_log-job_name-input',
                                                            placeholder='请输入任务名称',
                                                            autoComplete='off',
                                                            allowClear=True,
                                                            style={
                                                                'width': 240
                                                            }
                                                        ),
                                                        label='任务名称',
                                                        style={'paddingBottom': '10px'},
                                                    ),
                                                    fac.AntdFormItem(
                                                        fac.AntdSelect(
                                                            id='job_log-job_group-select',
                                                            placeholder='请选择任务组名',
                                                            options=[],
                                                            style={
                                                                'width': 240
                                                            }
                                                        ),
                                                        label='任务组名',
                                                        style={'paddingBottom': '10px'},
                                                    ),
                                                    fac.AntdFormItem(
                                                        fac.AntdSelect(
                                                            id='job_log-status-select',
                                                            placeholder='请选择执行状态',
                                                            options=[
                                                                {
                                                                    'label': '成功',
                                                                    'value': '0'
                                                                },
                                                                {
                                                                    'label': '失败',
                                                                    'value': '1'
                                                                }
                                                            ],
                                                            style={
                                                                'width': 240
                                                            }
                                                        ),
                                                        label='执行状态',
                                                        style={'paddingBottom': '10px'},
                                                    ),
                                                    fac.AntdFormItem(
                                                        fac.AntdDateRangePicker(
                                                            id='job_log-create_time-range',
                                                            style={
                                                                'width': 240
                                                            }
                                                        ),
                                                        label='执行时间',
                                                        style={'paddingBottom': '10px'},
                                                    ),
                                                    fac.AntdFormItem(
                                                        fac.AntdButton(
                                                            '搜索',
                                                            id='job_log-search',
                                                            type='primary',
                                                            icon=fac.AntdIcon(
                                                                icon='antd-search'
                                                            )
                                                        ),
                                                        style={'paddingBottom': '10px'},
                                                    ),
                                                    fac.AntdFormItem(
                                                        fac.AntdButton(
                                                            '重置',
                                                            id='job_log-reset',
                                                            icon=fac.AntdIcon(
                                                                icon='antd-sync'
                                                            )
                                                        ),
                                                        style={'paddingBottom': '10px'},
                                                    )
                                                ],
                                                layout='inline',
                                            )
                                        ],
                                        id='job_log-search-form-container',
                                        hidden=False
                                    ),
                                )
                            ]
                        ),
                        fac.AntdRow(
                            [
                                fac.AntdCol(
                                    fac.AntdSpace(
                                        [
                                            html.Div(
                                                [
                                                    fac.AntdButton(
                                                        [
                                                            fac.AntdIcon(
                                                                icon='antd-delete'
                                                            ),
                                                            '删除',
                                                        ],
                                                        id='job_log-delete',
                                                        disabled=True,
                                                        style={
                                                            'color': '#ff9292',
                                                            'background': '#ffeded',
                                                            'border-color': '#ffdbdb'
                                                        }
                                                    ),
                                                ],
                                                hidden='monitor:job:remove' not in button_perms
                                            ),
                                            html.Div(
                                                [
                                                    fac.AntdButton(
                                                        [
                                                            fac.AntdIcon(
                                                                icon='antd-clear'
                                                            ),
                                                            '清空',
                                                        ],
                                                        id='job_log-clear',
                                                        style={
                                                            'color': '#ff9292',
                                                            'background': '#ffeded',
                                                            'border-color': '#ffdbdb'
                                                        }
                                                    ),
                                                ],
                                                hidden='monitor:job:remove' not in button_perms
                                            ),
                                            html.Div(
                                                [
                                                    fac.AntdButton(
                                                        [
                                                            fac.AntdIcon(
                                                                icon='antd-arrow-down'
                                                            ),
                                                            '导出',
                                                        ],
                                                        id='job_log-export',
                                                        style={
                                                            'color': '#ffba00',
                                                            'background': '#fff8e6',
                                                            'border-color': '#ffe399'
                                                        }
                                                    ),
                                                ],
                                                hidden='monitor:job:export' not in button_perms
                                            ),
                                        ],
                                        style={
                                            'paddingBottom': '10px'
                                        }
                                    ),
                                    span=16
                                ),
                                fac.AntdCol(
                                    fac.AntdSpace(
                                        [
                                            html.Div(
                                                fac.AntdTooltip(
                                                    fac.AntdButton(
                                                        [
                                                            fac.AntdIcon(
                                                                icon='antd-search'
                                                            ),
                                                        ],
                                                        id='job_log-hidden',
                                                        shape='circle'
                                                    ),
                                                    id='job_log-hidden-tooltip',
                                                    title='隐藏搜索'
                                                )
                                            ),
                                            html.Div(
                                                fac.AntdTooltip(
                                                    fac.AntdButton(
                                                        [
                                                            fac.AntdIcon(
                                                                icon='antd-sync'
                                                            ),
                                                        ],
                                                        id='job_log-refresh',
                                                        shape='circle'
                                                    ),
                                                    title='刷新'
                                                )
                                            ),
                                        ],
                                        style={
                                            'float': 'right',
                                            'paddingBottom': '10px'
                                        }
                                    ),
                                    span=8,
                                    style={
                                        'paddingRight': '10px'
                                    }
                                )
                            ],
                            gutter=5
                        ),
                        fac.AntdRow(
                            [
                                fac.AntdCol(
                                    fac.AntdSpin(
                                        fac.AntdTable(
                                            id='job_log-list-table',
                                            data=[],
                                            columns=[
                                                {
                                                    'dataIndex': 'job_log_id',
                                                    'title': '日志编号',
                                                    'renderOptions': {
                                                        'renderType': 'ellipsis'
                                                    },
                                                },
                                                {
                                                    'dataIndex': 'job_name',
                                                    'title': '任务名称',
                                                    'renderOptions': {
                                                        'renderType': 'ellipsis'
                                                    },
                                                },
                                                {
                                                    'dataIndex': 'job_group',
                                                    'title': '任务组名',
                                                    'renderOptions': {
                                                        'renderType': 'tags'
                                                    },
                                                },
                                                {
                                                    'dataIndex': 'invoke_target',
                                                    'title': '调用目标字符串',
                                                    'renderOptions': {
                                                        'renderType': 'ellipsis'
                                                    },
                                                },
                                                {
                                                    'dataIndex': 'job_message',
                                                    'title': '日志信息',
                                                    'renderOptions': {
                                                        'renderType': 'ellipsis'
                                                    },
                                                },
                                                {
                                                    'dataIndex': 'status',
                                                    'title': '执行状态',
                                                    'renderOptions': {
                                                        'renderType': 'tags'
                                                    },
                                                },
                                                {
                                                    'dataIndex': 'create_time',
                                                    'title': '执行时间',
                                                    'renderOptions': {
                                                        'renderType': 'ellipsis'
                                                    },
                                                },
                                                {
                                                    'title': '操作',
                                                    'dataIndex': 'operation',
                                                    'renderOptions': {
                                                        'renderType': 'button'
                                                    },
                                                }
                                            ],
                                            rowSelectionType='checkbox',
                                            rowSelectionWidth=50,
                                            bordered=True,
                                            pagination={
                                                'pageSize': 10,
                                                'current': 1,
                                                'showSizeChanger': True,
                                                'pageSizeOptions': [10, 30, 50, 100],
                                                'showQuickJumper': True,
                                                'total': 0
                                            },
                                            mode='server-side',
                                            style={
                                                'width': '100%',
                                                'padding-right': '10px'
                                            }
                                        ),
                                        text='数据加载中'
                                    ),
                                )
                            ]
                        ),
                    ],
                    span=24
                )
            ],
            gutter=5
        ),

        # 任务调度日志明细modal
        fac.AntdModal(
            [
                fac.AntdForm(
                    [
                        fac.AntdRow(
                            [
                                fac.AntdCol(
                                    fac.AntdFormItem(
                                        fac.AntdText(id='job_log-job_name-text'),
                                        label='任务名称',
                                        required=True,
                                        id='job_log-job_name-form-item',
                                        labelCol={
                                            'span': 8
                                        },
                                        wrapperCol={
                                            'span': 16
                                        }
                                    ),
                                    span=12
                                ),
                                fac.AntdCol(
                                    fac.AntdFormItem(
                                        fac.AntdText(id='job_log-job_group-text'),
                                        label='任务分组',
                                        required=True,
                                        id='job_log-job_group-form-item',
                                        labelCol={
                                            'span': 8
                                        },
                                        wrapperCol={
                                            'span': 16
                                        }
                                    ),
                                    span=12
                                ),
                            ],
                            gutter=5
                        ),
                        fac.AntdRow(
                            [
                                fac.AntdCol(
                                    fac.AntdFormItem(
                                        fac.AntdText(id='job_log-job_executor-text'),
                                        label='任务执行器',
                                        required=True,
                                        id='job_log-job_executor-form-item',
                                        labelCol={
                                            'span': 8
                                        },
                                        wrapperCol={
                                            'span': 16
                                        }
                                    ),
                                    span=12
                                ),
                                fac.AntdCol(
                                    fac.AntdFormItem(
                                        fac.AntdText(id='job_log-invoke_target-text'),
                                        label='调用目标字符串',
                                        required=True,
                                        id='job_log-invoke_target-form-item',
                                        labelCol={
                                            'span': 8
                                        },
                                        wrapperCol={
                                            'span': 16
                                        }
                                    ),
                                    span=12
                                ),
                            ],
                            gutter=5
                        ),
                        fac.AntdRow(
                            [
                                fac.AntdCol(
                                    fac.AntdFormItem(
                                        fac.AntdText(id='job_log-job_args-text'),
                                        label='位置参数',
                                        required=True,
                                        id='job_log-job_args-form-item',
                                        labelCol={
                                            'span': 8
                                        },
                                        wrapperCol={
                                            'span': 16
                                        }
                                    ),
                                    span=12
                                ),
                                fac.AntdCol(
                                    fac.AntdFormItem(
                                        fac.AntdText(id='job_log-job_kwargs-text'),
                                        label='关键字参数',
                                        required=True,
                                        id='job_log-job_kwargs-form-item',
                                        labelCol={
                                            'span': 8
                                        },
                                        wrapperCol={
                                            'span': 16
                                        }
                                    ),
                                    span=12
                                ),
                            ],
                            gutter=5
                        ),
                        fac.AntdRow(
                            [
                                fac.AntdCol(
                                    fac.AntdFormItem(
                                        fac.AntdText(id='job_log-job_trigger-text'),
                                        label='任务触发器',
                                        required=True,
                                        id='job_log-job_trigger-form-item',
                                        labelCol={
                                            'span': 4
                                        },
                                        wrapperCol={
                                            'span': 20
                                        }
                                    ),
                                    span=24
                                ),
                            ],
                        ),
                        fac.AntdRow(
                            [
                                fac.AntdCol(
                                    fac.AntdFormItem(
                                        fac.AntdText(id='job_log-job_message-text'),
                                        label='日志信息',
                                        required=True,
                                        id='job_log-job_message-form-item',
                                        labelCol={
                                            'span': 4
                                        },
                                        wrapperCol={
                                            'span': 20
                                        }
                                    ),
                                    span=24
                                ),
                            ],
                        ),
                        fac.AntdRow(
                            [
                                fac.AntdCol(
                                    fac.AntdFormItem(
                                        fac.AntdText(id='job_log-status-text'),
                                        label='执行状态',
                                        required=True,
                                        id='job_log-status-form-item',
                                        labelCol={
                                            'span': 8
                                        },
                                        wrapperCol={
                                            'span': 16
                                        }
                                    ),
                                    span=12
                                ),
                                fac.AntdCol(
                                    fac.AntdFormItem(
                                        fac.AntdText(id='job_log-create_time-text'),
                                        label='执行时间',
                                        required=True,
                                        id='job_log-create_time-form-item',
                                        labelCol={
                                            'span': 8
                                        },
                                        wrapperCol={
                                            'span': 16
                                        }
                                    ),
                                    span=12
                                ),
                            ],
                            gutter=5
                        ),
                        fac.AntdRow(
                            [
                                fac.AntdCol(
                                    fac.AntdFormItem(
                                        fac.AntdText(id='job_log-exception_info-text'),
                                        label='异常信息',
                                        required=True,
                                        id='job_log-exception_info-form-item',
                                        labelCol={
                                            'span': 4
                                        },
                                        wrapperCol={
                                            'span': 20
                                        }
                                    ),
                                    span=24
                                ),
                            ],
                        ),
                    ],
                    labelCol={
                        'span': 8
                    },
                    wrapperCol={
                        'span': 16
                    },
                    style={
                        'marginRight': '15px'
                    }
                )
            ],
            id='job_log-modal',
            mask=False,
            width=850,
            renderFooter=False,
        ),

        # 删除任务调度日志二次确认modal
        fac.AntdModal(
            fac.AntdText('是否确认删除？', id='job_log-delete-text'),
            id='job_log-delete-confirm-modal',
            visible=False,
            title='提示',
            renderFooter=True,
            centered=True
        ),
    ]
