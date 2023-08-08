from fastapi import APIRouter, Request
from fastapi import Depends, Header
from config.get_db import get_db
from module_admin.service.login_service import get_current_user
from module_admin.service.log_service import *
from module_admin.entity.vo.log_vo import *
from utils.response_util import *
from utils.log_util import *
from utils.page_util import get_page_obj
from module_admin.aspect.interface_auth import CheckUserInterfaceAuth
from module_admin.annotation.log_annotation import log_decorator


logController = APIRouter(prefix='/log', dependencies=[Depends(get_current_user)])


@logController.post("/operation/get", response_model=OperLogPageObjectResponse, dependencies=[Depends(CheckUserInterfaceAuth('monitor:operlog:list'))])
async def get_system_operation_log_list(request: Request, operation_log_page_query: OperLogPageObject, query_db: Session = Depends(get_db)):
    try:
        # 获取全量数据
        operation_log_query_result = get_operation_log_list_services(query_db, operation_log_page_query)
        # 分页操作
        operation_log_page_query_result = get_page_obj(operation_log_query_result, operation_log_page_query.page_num, operation_log_page_query.page_size)
        logger.info('获取成功')
        return response_200(data=operation_log_page_query_result, message="获取成功")
    except Exception as e:
        logger.exception(e)
        return response_500(data="", message="接口异常")


@logController.post("/operation/delete", response_model=CrudLogResponse, dependencies=[Depends(CheckUserInterfaceAuth('monitor:operlog:remove'))])
@log_decorator(title='操作日志管理', business_type=3)
async def delete_system_operation_log(request: Request, delete_operation_log: DeleteOperLogModel, query_db: Session = Depends(get_db)):
    try:
        delete_operation_log_result = delete_operation_log_services(query_db, delete_operation_log)
        if delete_operation_log_result.is_success:
            logger.info(delete_operation_log_result.message)
            return response_200(data=delete_operation_log_result, message=delete_operation_log_result.message)
        else:
            logger.warning(delete_operation_log_result.message)
            return response_400(data="", message=delete_operation_log_result.message)
    except Exception as e:
        logger.exception(e)
        return response_500(data="", message="接口异常")


@logController.post("/operation/clear", response_model=CrudLogResponse, dependencies=[Depends(CheckUserInterfaceAuth('monitor:operlog:remove'))])
@log_decorator(title='操作日志管理', business_type=9)
async def clear_system_operation_log(request: Request, clear_operation_log: ClearOperLogModel, query_db: Session = Depends(get_db)):
    try:
        clear_operation_log_result = clear_operation_log_services(query_db, clear_operation_log)
        if clear_operation_log_result.is_success:
            logger.info(clear_operation_log_result.message)
            return response_200(data=clear_operation_log_result, message=clear_operation_log_result.message)
        else:
            logger.warning(clear_operation_log_result.message)
            return response_400(data="", message=clear_operation_log_result.message)
    except Exception as e:
        logger.exception(e)
        return response_500(data="", message="接口异常")


@logController.get("/operation/{oper_id}", response_model=OperLogModel, dependencies=[Depends(CheckUserInterfaceAuth('monitor:operlog:query'))])
async def query_detail_system_operation_log(request: Request, oper_id: int, query_db: Session = Depends(get_db)):
    try:
        detail_operation_log_result = detail_operation_log_services(query_db, oper_id)
        logger.info(f'获取oper_id为{oper_id}的信息成功')
        return response_200(data=detail_operation_log_result, message='获取成功')
    except Exception as e:
        logger.exception(e)
        return response_500(data="", message="接口异常")


@logController.post("/login/get", response_model=LoginLogPageObjectResponse, dependencies=[Depends(CheckUserInterfaceAuth('monitor:logininfor:list'))])
async def get_system_login_log_list(request: Request, login_log_page_query: LoginLogPageObject, query_db: Session = Depends(get_db)):
    try:
        # 获取全量数据
        login_log_query_result = get_login_log_list_services(query_db, login_log_page_query)
        # 分页操作
        login_log_page_query_result = get_page_obj(login_log_query_result, login_log_page_query.page_num, login_log_page_query.page_size)
        logger.info('获取成功')
        return response_200(data=login_log_page_query_result, message="获取成功")
    except Exception as e:
        logger.exception(e)
        return response_500(data="", message="接口异常")


@logController.post("/login/delete", response_model=CrudLogResponse, dependencies=[Depends(CheckUserInterfaceAuth('monitor:logininfor:remove'))])
@log_decorator(title='登录日志管理', business_type=3)
async def delete_system_login_log(request: Request, delete_login_log: DeleteLoginLogModel, query_db: Session = Depends(get_db)):
    try:
        delete_login_log_result = delete_login_log_services(query_db, delete_login_log)
        if delete_login_log_result.is_success:
            logger.info(delete_login_log_result.message)
            return response_200(data=delete_login_log_result, message=delete_login_log_result.message)
        else:
            logger.warning(delete_login_log_result.message)
            return response_400(data="", message=delete_login_log_result.message)
    except Exception as e:
        logger.exception(e)
        return response_500(data="", message="接口异常")


@logController.post("/login/clear", response_model=CrudLogResponse, dependencies=[Depends(CheckUserInterfaceAuth('monitor:logininfor:remove'))])
@log_decorator(title='登录日志管理', business_type=9)
async def clear_system_login_log(request: Request, clear_login_log: ClearLoginLogModel, query_db: Session = Depends(get_db)):
    try:
        clear_login_log_result = clear_login_log_services(query_db, clear_login_log)
        if clear_login_log_result.is_success:
            logger.info(clear_login_log_result.message)
            return response_200(data=clear_login_log_result, message=clear_login_log_result.message)
        else:
            logger.warning(clear_login_log_result.message)
            return response_400(data="", message=clear_login_log_result.message)
    except Exception as e:
        logger.exception(e)
        return response_500(data="", message="接口异常")
